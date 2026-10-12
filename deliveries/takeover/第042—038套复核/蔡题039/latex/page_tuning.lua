-- Convert hidden Markdown compact-block comments into local LaTeX spacing
-- settings. The markers stay invisible in Obsidian and avoid leaving a final
-- formula or one sentence alone on a new page without intruding into margins.

function RawBlock(element)
  if element.format ~= "html" then
    return nil
  end

  if string.match(element.text, "PAGE_COMPACT_START") then
    return pandoc.RawBlock(
      "latex",
      table.concat({
        "\\begingroup",
        "\\setlength{\\abovedisplayskip}{2pt plus 1pt minus 1pt}",
        "\\setlength{\\belowdisplayskip}{2pt plus 1pt minus 1pt}",
        "\\setlength{\\abovedisplayshortskip}{1pt plus 1pt}",
        "\\setlength{\\belowdisplayshortskip}{1pt plus 1pt}",
        "\\setlength{\\parskip}{0pt}",
        "\\setstretch{1.0}",
        "\\setlist{itemsep=0pt,topsep=0pt}"
      }, "\n")
    )
  end

  if string.match(element.text, "PAGE_COMPACT_END") then
    return pandoc.RawBlock("latex", "\\endgroup")
  end

  return nil
end
