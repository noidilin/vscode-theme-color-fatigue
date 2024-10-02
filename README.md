# Color Fatigue Dark Theme

## Overview

The Color Fatigue Dark theme is designed for developers who appreciate a calm, understated aesthetic. It’s perfect for those late-night coding marathons when you want to maintain focus without overwhelming your senses.

### Key Characteristics

- **Desaturated Colors**: I’ve intentionally toned down the vibrancy. Expect muted hues that won’t shout at you from the screen.
- **Low Contrast**: The contrast between foreground and background elements is gentle. No stark white on black here — just soothing shades that blend harmoniously.

### Theme Preview

> File Icons: I use [Quill Icons](https://github.com/cdonohue/vscode-quill-icons) as my icon. Feel free to try out different icons in the marketplace.

![broad view](https://raw.githubusercontent.com/noidilin/vscode-theme-color-fatigue/main/img/broad-view.jpg)
![terminal](https://raw.githubusercontent.com//noidilin/vscode-theme-color-fatigue/main/img/terminal.jpg)

### How to Apply

1. Open Visual Studio Code.
2. Navigate to File > Preferences > Color Theme.
3. Select "Color Fatigue Dark" from the theme picker.
4. Enjoy coding in tranquility!

---

## Color Palette

> Color palette is designed to utilize existing catppuccin-mocha theme. Replacing colors based on the table can often gives you pretty good start point for further customization.

### Saturation

- gogh-apprentice
- ref: http://gogh-co.github.io/Gogh/
- normal: https://coolors.co/b3ad9f-b07878-c8a492-d6caab-778777-7d96ad-797994-769494
- bright: https://coolors.co/dad5c8-cc9393-dcb5a5-ebd6b7-9bb09b-9db2cf-9f9fbd-92b3b3

| hex     | terminal   | mocha    | hex     | terminal       | mocha     |
| ------- | ---------- | -------- | ------- | -------------- | --------- |
| #b3b3b3 | foreground |          | #191919 | background     |           |
| #eaeaea | cursor     |          | #303030 | selection      |           |
| #474747 | black      |          | #5d5d5d | black-bright   |           |
| #dad5c8 | white      |          | #faf5eb | white-bright   |           |
| #b07878 | red        | red      | #cc9393 | red-bright     | maroon    |
| #778777 | green      | green    | #9bb09b | green-bright   | teal      |
| #d6caab | yellow     | peach    | #ebd6b7 | yellow-bright  | yellow    |
| #7d96ad | blue       | blue     | #9db2cf | blue-bright    | lavender  |
| #797994 | magenta    | mauve    | #9f9fbd | magenta-bright | pink      |
| #769494 | cyan       | sapphire | #92b3b3 | cyan-bright    | sky       |
| #c8a492 | orange     | flamingo | #dcb5a5 | orange-bright  | rosewater |

### Accent

| hex-accent | description   | hex-dim | description                                 |
| ---------- | ------------- | ------- | ------------------------------------------- |
| #faf5eb    |               | #f7f4ed |                                             |
| #dad5c8    |               | #d6d3cc |                                             |
| #c0baad    |               | #bdbab2 |                                             |
| #b3ad9f    | info, changed | #b4b0a7 | constant                                    |
| #a69f91    |               | #a19d97 |                                             |
| #9a9487    |               | #97948c |                                             |
| #8e897d    |               | #8e8b85 | func-call, var-other, JSX bracket, md-quote |
| #7f7b70    |               | #7b7974 |                                             |
| #706c62    |               | #6c6a65 |                                             |

### Monochrome

| hex     | description                                               | mocha    |
| ------- | --------------------------------------------------------- | -------- |
| #eaeaea | type, class-lib, const-deSat,                             |          |
| #dcdcdc | tag-name, css-func                                        |          |
| #cccccc |                                                           |          |
| #c0c0c0 | func-name, class-inherited, tag-ID, css-value             |          |
| #b3b3b3 |                                                           | text     |
| #aaaaaa | separator, regex-escape, md-raw                           |          |
| #9d9d9d | keyword, var-lang, tag-attr, JSON, md-heading             | subtext1 |
| #8e8e8e |                                                           |          |
| #878787 | class, pkg, var, param, num, css-pseudo+prop, js-temp-str | subtext0 |
| #7f7f7f |                                                           |          |
| #707070 | string, css-string, link, regex                           | overlay2 |
| #686868 | comment-emphasis, css-unit                                |          |
| #5d5d5d | embedded-string, md-separator                             | overlay1 |
| #555555 | comment, md-punctuation                                   |          |
| #4e4e4e |                                                           | overlay0 |
| #474747 |                                                           |          |
| #414141 |                                                           | surface2 |
| #3a3a3a |                                                           |          |
| #353535 |                                                           | surface1 |
| #303030 |                                                           |          |
| #2a2a2a |                                                           | surface0 |
| #242424 |                                                           |          |
| #1e1e1e |                                                           | base     |
| #191919 |                                                           | mantle   |
| #151515 |                                                           | crust    |
| #101010 |                                                           |          |

---

## Specials Thanks

This theme is inspired these the great theme:

- [Monochrom](https://github.com/anotherglitchinthematrix/monochrome)
- [Vitesse](https://github.com/antfu/vscode-theme-vitesse)
- [Gruvbox Concoctis](https://github.com/wheredoesyourmindgo/gruvbox-concoctis-vscode-theme)
- [Github VSC Theme](https://github.com/primer/github-vscode-theme?tab=readme-ov-file)

With these great reference, I basically hand code every value that I preferred. Hope I can get better in programming that one day I can make this process more efficient.

> Remember, this theme is all about balance—subdued yet functional. Let it soothe your tired programmer eyes as you craft elegant code. 🌿
> Feel free to give it a try, and let me know if you’d like any adjustments or additional details! 😊
