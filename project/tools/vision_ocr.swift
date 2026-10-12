import AppKit
import Foundation
import Vision

func recognize(_ path: String) throws -> [String] {
    let url = URL(fileURLWithPath: path)
    guard let image = NSImage(contentsOf: url) else {
        throw NSError(domain: "VisionOCR", code: 1, userInfo: [NSLocalizedDescriptionKey: "无法读取图像：\(path)"])
    }
    var rect = NSRect(origin: .zero, size: image.size)
    guard let cgImage = image.cgImage(forProposedRect: &rect, context: nil, hints: nil) else {
        throw NSError(domain: "VisionOCR", code: 2, userInfo: [NSLocalizedDescriptionKey: "无法转换图像：\(path)"])
    }

    var observations: [VNRecognizedTextObservation] = []
    var requestError: Error?
    let request = VNRecognizeTextRequest { request, error in
        requestError = error
        observations = request.results as? [VNRecognizedTextObservation] ?? []
    }
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["zh-Hans", "en-US"]

    try VNImageRequestHandler(cgImage: cgImage, options: [:]).perform([request])
    if let requestError {
        throw requestError
    }

    observations.sort { lhs, rhs in
        let dy = lhs.boundingBox.maxY - rhs.boundingBox.maxY
        if abs(dy) > 0.012 {
            return dy > 0
        }
        return lhs.boundingBox.minX < rhs.boundingBox.minX
    }
    return observations.compactMap { $0.topCandidates(1).first?.string }
}

let arguments = Array(CommandLine.arguments.dropFirst())
guard !arguments.isEmpty else {
    FileHandle.standardError.write(Data("用法：vision_ocr image...\n".utf8))
    exit(2)
}

for path in arguments {
    print("===== \(path) =====")
    do {
        for line in try recognize(path) {
            print(line)
        }
    } catch {
        FileHandle.standardError.write(Data("OCR 失败：\(path)：\(error)\n".utf8))
        exit(1)
    }
}
