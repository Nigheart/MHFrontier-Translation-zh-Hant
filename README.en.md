# Monster Hunter Frontier ZZ · Traditional Chinese Text Dataset

**MHFrontier-Translation-zh-Hant**

[简体中文](README.md) | **English**

---

Traditional Chinese text data for the PC offline release of *Monster Hunter Frontier ZZ* (MHFCN / MHZZ).

The game carries **107,222** entries for weapons, armor, materials and items. Their names,
descriptions and acquisition text are collected here as CSV files, grouped by the game's own
data tables.

The data can serve as a text source for translation patches, or be used for proofreading,
glossary work and other tooling. The game itself, its launcher, and any prebuilt patch are
not part of this repository.

| | |
|---|---|
| Entries covered | **107,222** |
| Names filled | 88,944 |
| Descriptions translated | 98,069 |
| Placeholder descriptions (dummy / no translation needed) | 9,153 |
| Residual kana / CP932 encoding failures | **0 / 0** |
| Text fields in total | 392,065 |

---

## Layout

```
.
├── translations/
│   └── zh-Hant/                 Traditional Chinese translations
│       ├── armors/
│       │   ├── head.csv         Armor · Head        (14,594 entries)
│       │   ├── body.csv         Armor · Body        (13,462 entries)
│       │   ├── arms.csv         Armor · Arms        (13,452 entries)
│       │   ├── waist.csv        Armor · Waist       (13,708 entries)
│       │   └── legs.csv         Armor · Legs        (13,514 entries)
│       ├── weapons/
│       │   ├── melee.csv        Weapons · Melee     (17,568 entries)
│       │   └── ranged.csv       Weapons · Ranged    (4,223 entries)
│       └── items/
│           ├── materials.csv    Materials · monsters, creatures, ore (1,074)
│           ├── decorations.csv  Decorations                          (5,245)
│           ├── unclassified.csv Unclassified items and materials     (8,952)
│           └── others.csv       Other items                          (1,430)
└── docs/
    ├── 术语表与译名对照.md         glossary: monster / material / item / part names
    ├── 怪物素材物品四语对照表.md    four-language table (JA / ZH-Hant / EN / ZH-Hans)
    ├── 怪物素材物品四语对照表.csv
    ├── 最终审计报告.txt            final audit report
    └── reports/                  per-stage review and re-translation reports
```

---

## Data format

Each CSV has **11 columns** and is UTF-8 encoded:

| Column | Meaning |
|---|---|
| `条目ID` | Stable entry ID, used to align with upstream projects |
| `游戏ID（十进制）` / `游戏ID（十六进制）` | Byte offset identifier inside `mhfdat.bin` |
| `分类` | Fine-grained in-game category (e.g. monster material, decoration) |
| `当前名称` | Text before this change (previous translation or original) |
| `精翻名称（在此填写）` | **Current translation — name** |
| `当前说明` | Description before this change |
| `精翻说明（在此填写）` | **Current translation — description** (`\n` is an in-game line break) |
| `当前获取途径` | Acquisition text before this change |
| `精翻获取途径（在此填写）` | **Current translation — acquisition** |
| `备注` | Translator notes, usually the reasoning behind a decision |

Because "current" and "translated" are paired columns, **any two versions can be diffed directly**,
and the effect of a change is visible at a glance.

> `~C05 … ~C00` sequences are in-game text color codes, not mojibake.
> `≪…≫` marks are client-side emphasis and must be preserved verbatim.

---

## Sources and credits

Parts of the text and content in this project come from the two sources below.

### 1. Upstream text project

[**Mogapedia / MHFrontier-Translation**](https://github.com/Mogapedia/MHFrontier-Translation) (GPL-3.0)

Provides the full Japanese source text and an English reference (about 10,853 entries, 94.7% coverage).
It is the primary translation basis for this project.

Additional references:

- `mhwiki.axibug.com/MHFZCN/sozai/item.js` — Japanese item text (8,516 entries)
- [rekowiki.org](https://rekowiki.org) — Japanese ↔ Traditional Chinese monster names
- [monsterhunterwiki.org](https://monsterhunterwiki.org) — English names

### 2. Bilibili all-in-one release

[**【汉化发布】PC《怪物猎人 边境ZZ》 单机整合终极版**](https://www.bilibili.com/video/BV1xSWa6aErK)
by [metalmouse](https://space.bilibili.com/66745548)

That release handled offline conversion, the launcher, server adaptation and a first-pass
Chinese translation (about 90% of UI / story / items / quests / images). This project continues
from its text to fully re-translate equipment and item names and descriptions.

Copyright of the all-in-one release and of the game itself belongs to its authors and to Capcom.
Neither is redistributed here.

### 3. Contributors

This project was mainly carried out by **DeepSeek 大肥鱼**: generating and rewriting translations,
deriving the glossary, devising workarounds for the limited CP932 character set, and running all
validation.

---

## Translation conventions

In-game text is written in **CP932**, and the font table is a hard constraint.

### Use orthodox Traditional Chinese characters

`對 / 卻 / 搖 / 獲 / 說 / 歷` and similar stay in their orthodox forms. Automated substitution to
Japanese shinjitai (`対 / 却 / 揺 / 穫 / 説 / 歴`) is forbidden — an earlier script did that and
caused 334 semantic regressions, all of which have been reverted.

### Characters unavailable in CP932 must be paraphrased

| Wanted | Actually used |
|---|---|
| 盔 (helmet) | 兜 |
| 淚 / 溫 / 歷 / 歲 / 狀 / 戶 / 啟 | 涙 / 温 / 歴 / 歳 / 状 / 戸 / 啓 |
| 烤 (roast) | 燒 |
| 陷阱 (trap) | 罠 |
| 垃圾 / 醃 / 蜻蜓 / 靛 | 廢棄 / 漬 / 蜻蛉 / 藍 |

A further set of common Traditional characters (`說 內 絕 貓 靈 輝 雞 狀 …`) only exists in
Japanese forms in CP932, so those forms are used.

### Kana and English names are kept as-is

About 46,000 kana equipment names (`アメシスバイソンⅠ`, `ヴォトーⅡ`) have no reliable counterpart;
transliterating them would produce names nobody can verify, so they are preserved.
English names such as `Lethe` and `Zidoria` are treated the same way.

### Damaged source text is not rewritten

About 361 truncated names (`レ Arma斯庫`), about 19 fragmented descriptions and the shredded-paper
puzzles are kept verbatim rather than inventing meaning that the original does not have.

---

## Known gaps

1. 9,153 placeholders (`dummy` / `ダミー` / `※仮メッセージ` / dev-only strings) left as-is;
2. shredded-paper puzzles (14239–14241) and number puzzles (14346/14347) are encrypted kana strings;
3. some proper nouns in Fate collaboration equipment;
4. about 3,300 development placeholder entries;
5. some kana series names preserved (see above).

---

## Usage

- **Building a patch**: take `精翻名称`, `精翻说明` and `精翻获取途径` per `条目ID`, and write them
  back into the matching slots of `mhfdat.bin`. Empty values mean "keep the original text".
- **Proofreading**: compare the "current" and "translated" columns.
- **Glossaries**: see [`docs/术语表与译名对照.md`](docs/术语表与译名对照.md) and
  [`docs/怪物素材物品四语对照表.csv`](docs/怪物素材物品四语对照表.csv).

Writing back to `mhfdat.bin` requires CP932 encoding and pointer-table remapping; that part is
out of scope for this repository.

---

## License

This repository is released under **GPL-3.0**; see [LICENSE](LICENSE).

The primary upstream,
[Mogapedia / MHFrontier-Translation](https://github.com/Mogapedia/MHFrontier-Translation), is also
GPL-3.0, so the two are compatible. If you distribute a patch built from this data, the license
requires you to open-source the derivative work as well.

*Monster Hunter* is a trademark of **Capcom**. This is a non-commercial fan translation;
do not use it commercially. Launcher, trainer and offline-conversion patches related to the
Bilibili release belong to their respective authors.

---

## Credits

- [Mogapedia / MHFrontier-Translation](https://github.com/Mogapedia/MHFrontier-Translation) — Japanese source text and English reference
- [metalmouse](https://space.bilibili.com/66745548) — the *Monster Hunter Frontier ZZ* all-in-one release
- [mhwiki.axibug.com](https://mhwiki.axibug.com) / [rekowiki.org](https://rekowiki.org) / [monsterhunterwiki.org](https://monsterhunterwiki.org) — source and name references
- **DeepSeek 大肥鱼** — main translation and validation work
- and everyone still hunting on the Frontier

---

*A fan project. Not affiliated with Capcom or any of the sources listed above.*
