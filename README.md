# PlainText Journaling Markup Language

Inspired by Jeff Huang's idea of a productivity app as a never-ending .txt file [link](https://jeffhuang.com/productivity_text_file/) and influenced by Tony Stubblebine's concept of "interstitial journaling," the PlainText Journaling Markup Language is designed to simplify the experience of plain text journaling.

## Why?
I attempted a similar approach of that of Jeff, but found the unruliness of simple plain text lines lacking the necessary context cues. In response, I've crafted a straightforward syntax that maintains the ease of plain text while providing better organization and context for journaling.

## This Repository Includes
- **Simplicity with Context**: A plain text syntax that ensures clarity and context in your journal entries.
- **Ongoing Refinement**: The syntax is a work in progress, with continuous improvements planned for a more user-friendly experience.
- **Text Expander Tooling**: Future updates will include suggested text expander shortcuts for seamless and efficient journaling.
- **Draft Python Script**: A basic Python script is included for terminal-based manipulation. This script is in a proof-of-concept state, open for exploration and improvement.

## The Language Features
- Main headings underlined with equals(=) signs.
- Date formatting (e.g., 2023-11-14) underlined with equals sign initiates a new journal entry.
- Subheadings indicated by an underline of dashes.
- Allows plaintext and per-line thoughts with flexible organization using line breaks, indentation, or lists.
- Follows Markdown-like syntax for tasks.
- Additional task variations denoted by symbols (e.g., ! for important, !! for critical).
- Supports the creation of simple tables for structured data representation.
- Special syntax for recording meeting details, attendees, goals, notes, and tasks.
- Uses plus (+) sign for marking focus areas, facilitating easy search.
- Utilizes the @-sign for people and occasionally #-tags for miscellaneous notes.

Refer to syntax.txt in this repo for the full overview.

## Design Principles
The plaintext Journal Markup is written with the following in mind:

- Meant to be used in mono-spaced, plain text.
- Superbly lightweight and easily adopted.
- Avoid excessive wrapping of words in symbols. 
- Use symbols found on any keyboard.
- Prioritize white space for structure and clarity.
- Legible in any text editor.
- No excessive use of lists. Limit ‘outliner’ tendencies.
- Provide clear context indicators for lengthy journals.
- Emphasize writing and note-taking.

## Contribution
Feel free to contribute! Whether it's refining the syntax, suggesting improvements, or adding features, your input is welcome. Simply fork the project, make your changes, and submit a pull request.

## License
This project is open-source, and you are free to do whatever you want with it. Contributions are encouraged to make this a collaborative and robust tool for the community.