# 防具名修复对照表（225 条）

数据源：`_broken_names.tsv`（损坏名 / 日文原名 / 英文名）  

产出：`fixed_armor_names.json`（225 键，UTF-8 无 BOM）

## 一、统计

| 部位 | 条数 |
| --- | --- |
| 頭部 | 33 |
| 身體 | 15 |
| 腕部 | 128 |
| 腰部 | 38 |
| 腳部 | 11 |
| **合计** | **225** |

- 全部 225 条 `s.encode('cp932')` 通过；用字全部落在 JIS X 0208 标准区（0x81–0x9F / 0xE0–0xEA），不依赖 NEC/IBM 扩展区（0xED/0xEE），老旧字库也能显示。
- 显示宽度 225/225 均 ≤ 日文原名（最大节省 9 个半角宽）。
- 键集合与 TSV 完全一致：无缺失、无多余、无重名。

## 二、20 条典型对照

| 条目ID | 现有名（损坏） | 日文原名 | 新译名 |
| --- | --- | --- | --- |
| 头部防具:970 | `レ Arma斯庫・White` | レアルマスク・白 | **真實面具・白** |
| 头部防具:1065 | `Franc ト耳飾` | フラントピアス | **弗蘭特耳飾** |
| 头部防具:1380 | `Pasu マ面罩` | パスマフェイス | **霸斯瑪面罩** |
| 头部防具:2714 | `Ahaba ー耳飾` | アハバーピアス | **阿哈巴耳飾** |
| 头部防具:3084 | `ト Lea Piercings I` | トリアピアスⅠ | **托里亞耳飾Ⅰ** |
| 头部防具:3889 | `Shell カG兜` | シェルカＧヘッド | **謝爾嘉G兜** |
| 身体防具:1237 | `ス Fias茨` | スフィアスーツ | **斯菲亞服** |
| 身体防具:1682 | `エ Dios茨・Blue` | エディオスーツ・青 | **艾迪奧服・青** |
| 身体防具:4495 | `レ Disu茨・White` | レディスーツ・白 | **蕾蒂服・白** |
| 腕部防具:207 | `Kirin Sグ長袍` | キリンＳグローブ | **麒麟S手套** |
| 腕部防具:1025 | `阿魯Jyaga ド` | アルジャガード | **阿爾賈加多腕甲** |
| 腕部防具:2028 | `Shadow Fグ長袍Purple` | シャドウＦグローブ紫 | **暗影F手套紫** |
| 腕部防具:6560 | `Truss FZグ長袍Blue` | トラスFZグローブ青 | **特拉斯FZ手套青** |
| 腰部防具:1735 | `Steno Elytra ー・Orange` | ステノアンカー・橙 | **斯特諾錨・橙** |
| 腰部防具:4244 | `Steno HS Elytra ー・Blue` | ステノHSアンカー・青 | **斯特諾HS錨・青** |
| 脚部防具:555 | `リ Anbu茨・Blue` | リアンブーツ・青 | **莉安靴・青** |
| 脚部防具:1146 | `Pasu マ護腿` | パスマフット | **霸斯瑪足** |
| 脚部防具:1396 | `マ Sharufu托` | マシャルフット | **馬沙爾足** |
| 脚部防具:3337 | `ロ Black Blos G護腿` | ロアースＧレッグ | **羅亞斯G腿甲** |
| 身体防具:3342 | `ロ Black Blos G鎧甲` | ロアースＧメイル | **羅亞斯G鎧甲** |

## 三、译名构件（保证同一假名序列 -> 同一中文）

| 日文 | 中文 | 依据 |
| --- | --- | --- |
| レアル | 真實 | real |
| フラント | 弗蘭特 | 音译 |
| パスマ | 霸斯瑪 | 音译（帕不可用，见踩坑） |
| アハバー | 阿哈巴 | 音译 |
| トリア | 托里亞 | 音译 |
| シェルカ | 謝爾嘉 | 音译（卡不可用） |
| ロアース | 羅亞斯 | 音译 |
| スフィア | 斯菲亞 | 音译 |
| エディオ | 艾迪奧 | 音译 |
| レディ | 蕾蒂 | Lady |
| キリン | 麒麟 | 原字 |
| ルルディ | 露露迪 | 音译 |
| トラス | 特拉斯 | 音译 |
| シャドウ | 暗影 | Shadow |
| ソウル | 靈魂 | Soul |
| フレイ | 弗雷 | 音译 |
| ブリッツ | 閃電 | Blitz |
| ブルック | 布魯克 | 音译 |
| ガウシカ | 加烏希嘉 | Anteka |
| ルフレ | 露弗雷 | 音译 |
| ゴルック | 戈魯克 | 音译 |
| スフレ | 斯弗雷 | 音译 |
| シルック | 希爾克 | 音译 |
| ノルック | 諾爾克 | 音译 |
| グレイ | 格雷 | Gray |
| ステノ | 斯特諾 | 音译 |
| リアン | 莉安 | 音译 |
| マシャル | 馬沙爾 | 音译 |
| アルジャガード | 阿爾賈加多 | jacquard，整条特例 |

| 部位词 | 中文 |
| --- | --- |
| ピアス | 耳飾 |
| フェイス | 面罩 |
| ヘッド | 兜 |
| メイル | 鎧甲 |
| アーム | 腕甲 |
| コイル | 腰甲 |
| グリーヴ | 護腿 |
| マスク | 面具 |
| ベスト | 背心 |
| スーツ | 服 |
| グローブ | 手套 |
| ブーツ | 靴 |
| フット | 足 |
| レッグ | 腿甲 |
| アンカー | 錨 |

等级后缀：`Ｆ→F`、`Ｇ→G`、`Ｓ→S`、`Ｌ→L`、`Ｄ→D`；`FZ/HC/HS/GS/GP/FX/FY/GF/GX` 原样保留（全角一律转半角）。  
颜色：`白→白`、`金→金`、`青→青`、`赤→赤`、`黄→黄`、`黒→黒`、`緑→緑`、`紫→紫`、`橙→橙`、`桃→桃`；原文有 `・` 的保留，无的不添加。

## 四、全量对照（225 条）

| 条目ID | 现有名（损坏） | 日文原名 | 新译名 | 英文名 |
| --- | --- | --- | --- | --- |
| 头部防具:970 | `レ Arma斯庫・White` | レアルマスク・白 | **真實面具・白** | Real Mask・White |
| 头部防具:974 | `レ Arma斯庫・Gold` | レアルマスク・金 | **真實面具・金** | Real Mask・Gold |
| 头部防具:978 | `レ Arma斯庫・Blue` | レアルマスク・青 | **真實面具・青** | Real Mask・Blue |
| 头部防具:982 | `レ Arma斯庫・Red` | レアルマスク・赤 | **真實面具・赤** | Real Mask・Red |
| 头部防具:1065 | `Franc ト耳飾` | フラントピアス | **弗蘭特耳飾** | フラント Piercing |
| 头部防具:1066 | `Franc トF耳飾` | フラントＦピアス | **弗蘭特F耳飾** | フラントF Piercing |
| 头部防具:1380 | `Pasu マ面罩` | パスマフェイス | **霸斯瑪面罩** | パスマ Face |
| 头部防具:1381 | `Pasu マF面罩` | パスマＦフェイス | **霸斯瑪F面罩** | パスマF Face |
| 头部防具:2714 | `Ahaba ー耳飾` | アハバーピアス | **阿哈巴耳飾** | Ahaba ー Piercing |
| 头部防具:2715 | `Ahaba ーF耳飾` | アハバーＦピアス | **阿哈巴F耳飾** | Ahaba ーF Piercing |
| 头部防具:3084 | `ト Lea Piercings I` | トリアピアスⅠ | **托里亞耳飾Ⅰ** | トリア Piercing I |
| 头部防具:3085 | `ト Lea F Piercings I` | トリアＦピアスⅠ | **托里亞F耳飾Ⅰ** | トリア F Piercing I |
| 头部防具:3086 | `ト Lea Piercings II` | トリアピアスⅡ | **托里亞耳飾Ⅱ** | トリア Piercing II |
| 头部防具:3087 | `ト Lea F Piercings II` | トリアＦピアスⅡ | **托里亞F耳飾Ⅱ** | トリア F Piercing II |
| 头部防具:3088 | `ト Lea Piercings III` | トリアピアスⅢ | **托里亞耳飾Ⅲ** | トリア Piercing III |
| 头部防具:3089 | `ト Lea F Piercings III` | トリアＦピアスⅢ | **托里亞F耳飾Ⅲ** | トリア F Piercing III |
| 头部防具:3090 | `ト Lea Piercings IV` | トリアピアスⅣ | **托里亞耳飾Ⅳ** | トリア Piercing IV |
| 头部防具:3091 | `ト Lea F Piercings IV` | トリアＦピアスⅣ | **托里亞F耳飾Ⅳ** | トリア F Piercing IV |
| 头部防具:3092 | `ト Lea Piercings V` | トリアピアスⅤ | **托里亞耳飾Ⅴ** | トリア Piercing V |
| 头部防具:3093 | `ト Lea F Piercings V` | トリアＦピアスⅤ | **托里亞F耳飾Ⅴ** | トリア F Piercing V |
| 头部防具:3094 | `ト Lea Piercings VI` | トリアピアスⅥ | **托里亞耳飾Ⅵ** | トリア Piercing VI |
| 头部防具:3095 | `ト Lea F Piercings VI` | トリアＦピアスⅥ | **托里亞F耳飾Ⅵ** | トリア F Piercing VI |
| 头部防具:3096 | `ト Lea Piercings VII` | トリアピアスⅦ | **托里亞耳飾Ⅶ** | トリア Piercing VII |
| 头部防具:3097 | `ト Lea F Piercings VII` | トリアＦピアスⅦ | **托里亞F耳飾Ⅶ** | トリア F Piercing VII |
| 头部防具:3098 | `ト Lea Piercings VIII` | トリアピアスⅧ | **托里亞耳飾Ⅷ** | トリア Piercing VIII |
| 头部防具:3099 | `ト Lea F Piercings VIII` | トリアＦピアスⅧ | **托里亞F耳飾Ⅷ** | トリア F Piercing VIII |
| 头部防具:3889 | `Shell カG兜` | シェルカＧヘッド | **謝爾嘉G兜** | シェルカG Head |
| 头部防具:3891 | `ロ Black Blos G兜` | ロアースＧヘッド | **羅亞斯G兜** | ロアース G Head |
| 头部防具:4099 | `Ahaba ーFZ耳飾` | アハバーFZピアス | **阿哈巴FZ耳飾** | Ahaba ーFZ Piercing |
| 头部防具:4100 | `Ahaba ーHC耳飾` | アハバーHCピアス | **阿哈巴HC耳飾** | Ahaba ーHC Piercing |
| 头部防具:4101 | `Ahaba ーHS耳飾` | アハバーHSピアス | **阿哈巴HS耳飾** | Ahaba ーHS Piercing |
| 头部防具:4516 | `Ahaba ーGS耳飾` | アハバーGSピアス | **阿哈巴GS耳飾** | Ahaba ーGS Piercing |
| 头部防具:7590 | `Ahaba ーGP耳飾` | アハバーGPピアス | **阿哈巴GP耳飾** | Ahaba ーGP Piercing |
| 身体防具:865 | `Franc ト鎧甲` | フラントメイル | **弗蘭特鎧甲** | フラント Mail |
| 身体防具:866 | `Franc トF鎧甲` | フラントＦメイル | **弗蘭特F鎧甲** | フラントF Mail |
| 身体防具:1152 | `Pasu マ背心` | パスマベスト | **霸斯瑪背心** | Pasu マ Vest |
| 身体防具:1153 | `Pasu マF背心` | パスマＦベスト | **霸斯瑪F背心** | Pasu マF Vest |
| 身体防具:1237 | `ス Fias茨` | スフィアスーツ | **斯菲亞服** | Sufia Suit |
| 身体防具:1682 | `エ Dios茨・Blue` | エディオスーツ・青 | **艾迪奧服・青** | エ Dios ーツ・Blue |
| 身体防具:1686 | `エ Dios茨・Red` | エディオスーツ・赤 | **艾迪奧服・赤** | エ Dios ーツ・Red |
| 身体防具:1690 | `エ Dios茨・Yellow` | エディオスーツ・黄 | **艾迪奧服・黄** | エ Dios ーツ・Yellow |
| 身体防具:1694 | `エ Dios茨・Black` | エディオスーツ・黒 | **艾迪奧服・黒** | エ Dios ーツ・Black |
| 身体防具:3340 | `Shell カG鎧甲` | シェルカＧメイル | **謝爾嘉G鎧甲** | Shell カG Mail |
| 身体防具:3342 | `ロ Black Blos G鎧甲` | ロアースＧメイル | **羅亞斯G鎧甲** | ロアースG Mail |
| 身体防具:4495 | `レ Disu茨・White` | レディスーツ・白 | **蕾蒂服・白** | Lady Suit・White |
| 身体防具:4519 | `レ Disu茨・Black` | レディスーツ・黒 | **蕾蒂服・黒** | Lady Suit・Black |
| 身体防具:4543 | `レ Disu茨・Red` | レディスーツ・赤 | **蕾蒂服・赤** | Lady Suit・Red |
| 身体防具:4567 | `レ Disu茨・Green` | レディスーツ・緑 | **蕾蒂服・緑** | Lady Suit・Green |
| 腕部防具:207 | `Kirin Sグ長袍` | キリンＳグローブ | **麒麟S手套** | Kirin Sグローブ |
| 腕部防具:861 | `Franc ト腕甲` | フラントアーム | **弗蘭特腕甲** | フラントArms |
| 腕部防具:862 | `Franc トF腕甲` | フラントＦアーム | **弗蘭特F腕甲** | フラントF Arms |
| 腕部防具:1025 | `阿魯Jyaga ド` | アルジャガード | **阿爾賈加多腕甲** | アル Jyaga ド |
| 腕部防具:1044 | `Kirin Lグ長袍` | キリンＬグローブ | **麒麟L手套** | Kirin Lグローブ |
| 腕部防具:1144 | `Pasu マ腕甲` | パスマアーム | **霸斯瑪腕甲** | Pasu マ Arms |
| 腕部防具:1145 | `Pasu マF腕甲` | パスマＦアーム | **霸斯瑪F腕甲** | Pasu マF Arms |
| 腕部防具:1904 | `ル Ledia穆` | ルルディアーム | **露露迪腕甲** | ル Ledia ーム |
| 腕部防具:1996 | `Truss Fグ長袍Blue` | トラスＦグローブ青 | **特拉斯F手套青** | Truss Fグローブ Blue |
| 腕部防具:2000 | `Truss Fグ長袍Red` | トラスＦグローブ赤 | **特拉斯F手套赤** | Truss Fグローブ Red |
| 腕部防具:2004 | `Truss Fグ長袍White` | トラスＦグローブ白 | **特拉斯F手套白** | Truss Fグローブ White |
| 腕部防具:2008 | `Truss Fグ長袍Purple` | トラスＦグローブ紫 | **特拉斯F手套紫** | Truss Fグローブ Purple |
| 腕部防具:2028 | `Shadow Fグ長袍Purple` | シャドウＦグローブ紫 | **暗影F手套紫** | Shadow Fグローブ Purple |
| 腕部防具:2030 | `Soul Fグ長袍Purple` | ソウルＦグローブ紫 | **靈魂F手套紫** | Soul Fグローブ Purple |
| 腕部防具:2032 | `Shadow Fグ長袍Red` | シャドウＦグローブ赤 | **暗影F手套赤** | Shadow Fグローブ Red |
| 腕部防具:2034 | `Soul Fグ長袍Red` | ソウルＦグローブ赤 | **靈魂F手套赤** | Soul Fグローブ Red |
| 腕部防具:2036 | `Shadow Fグ長袍Green` | シャドウＦグローブ緑 | **暗影F手套緑** | Shadow Fグローブ Green |
| 腕部防具:2038 | `Soul Fグ長袍Green` | ソウルＦグローブ緑 | **靈魂F手套緑** | Soul Fグローブ Green |
| 腕部防具:2040 | `Shadow Fグ長袍White` | シャドウＦグローブ白 | **暗影F手套白** | Shadow Fグローブ White |
| 腕部防具:2042 | `Soul Fグ長袍White` | ソウルＦグローブ白 | **靈魂F手套白** | Soul Fグローブ White |
| 腕部防具:2413 | `フ Rathian穆` | フレイアーム | **弗雷腕甲** | フ Rathian ーム |
| 腕部防具:2587 | `Blitz Fグ長袍` | ブリッツＦグローブ | **閃電F手套** | Blitz Fグローブ |
| 腕部防具:2741 | `Blitz FXグ長袍` | ブリッツFXグローブ | **閃電FX手套** | Blitz FXグローブ |
| 腕部防具:3335 | `Shell カG腕甲` | シェルカＧアーム | **謝爾嘉G腕甲** | Shell カG Arms |
| 腕部防具:3337 | `ロ Black Blos G腕甲` | ロアースＧアーム | **羅亞斯G腕甲** | ロアースG Arms |
| 腕部防具:3770 | `Blitz Gグ長袍` | ブリッツＧグローブ | **閃電G手套** | Blitz Gグローブ |
| 腕部防具:4488 | `レ Diablos穆・White` | レディアーム・白 | **蕾蒂腕甲・白** | Lady Arms・White |
| 腕部防具:4512 | `レ Diablos穆・Black` | レディアーム・黒 | **蕾蒂腕甲・黒** | Lady Arms・Black |
| 腕部防具:4536 | `レ Diablos穆・Red` | レディアーム・赤 | **蕾蒂腕甲・赤** | Lady Arms・Red |
| 腕部防具:4560 | `レ Diablos穆・Green` | レディアーム・緑 | **蕾蒂腕甲・緑** | Lady Arms・Green |
| 腕部防具:4708 | `Shadow FZグ長袍Purple` | シャドウFZグローブ紫 | **暗影FZ手套紫** | Shadow FZグローブ Purple |
| 腕部防具:4709 | `Shadow HSグ長袍Purple` | シャドウHSグローブ紫 | **暗影HS手套紫** | Shadow HSグローブ Purple |
| 腕部防具:4710 | `Shadow GSグ長袍Purple` | シャドウGSグローブ紫 | **暗影GS手套紫** | Shadow GSグローブ Purple |
| 腕部防具:4711 | `Shadow GPグ長袍Purple` | シャドウGPグローブ紫 | **暗影GP手套紫** | Shadow GPグローブ Purple |
| 腕部防具:4712 | `Soul FZグ長袍・Purple` | ソウルFZグローブ・紫 | **靈魂FZ手套・紫** | Soul FZグローブ・Purple |
| 腕部防具:4713 | `Soul HSグ長袍・Purple` | ソウルHSグローブ・紫 | **靈魂HS手套・紫** | Soul HSグローブ・Purple |
| 腕部防具:4714 | `Soul GSグ長袍・Purple` | ソウルGSグローブ・紫 | **靈魂GS手套・紫** | Soul GSグローブ・Purple |
| 腕部防具:4715 | `Soul GPグ長袍・Purple` | ソウルGPグローブ・紫 | **靈魂GP手套・紫** | Soul GPグローブ・Purple |
| 腕部防具:4724 | `Shadow FZグ長袍Red` | シャドウFZグローブ赤 | **暗影FZ手套赤** | Shadow FZグローブ Red |
| 腕部防具:4725 | `Shadow HSグ長袍Red` | シャドウHSグローブ赤 | **暗影HS手套赤** | Shadow HSグローブ Red |
| 腕部防具:4726 | `Shadow GSグ長袍Red` | シャドウGSグローブ赤 | **暗影GS手套赤** | Shadow GSグローブ Red |
| 腕部防具:4727 | `Shadow GPグ長袍Red` | シャドウGPグローブ赤 | **暗影GP手套赤** | Shadow GPグローブ Red |
| 腕部防具:4728 | `Soul FZグ長袍・Red` | ソウルFZグローブ・赤 | **靈魂FZ手套・赤** | Soul FZグローブ・Red |
| 腕部防具:4729 | `Soul HSグ長袍・Red` | ソウルHSグローブ・赤 | **靈魂HS手套・赤** | Soul HSグローブ・Red |
| 腕部防具:4730 | `Soul GSグ長袍・Red` | ソウルGSグローブ・赤 | **靈魂GS手套・赤** | Soul GSグローブ・Red |
| 腕部防具:4731 | `Soul GPグ長袍・Red` | ソウルGPグローブ・赤 | **靈魂GP手套・赤** | Soul GPグローブ・Red |
| 腕部防具:4740 | `Shadow FZグ長袍Green` | シャドウFZグローブ緑 | **暗影FZ手套緑** | Shadow FZグローブ Green |
| 腕部防具:4741 | `Shadow HSグ長袍Green` | シャドウHSグローブ緑 | **暗影HS手套緑** | Shadow HSグローブ Green |
| 腕部防具:4742 | `Shadow GSグ長袍Green` | シャドウGSグローブ緑 | **暗影GS手套緑** | Shadow GSグローブ Green |
| 腕部防具:4743 | `Shadow GPグ長袍Green` | シャドウGPグローブ緑 | **暗影GP手套緑** | Shadow GPグローブ Green |
| 腕部防具:4744 | `Soul FZグ長袍・Green` | ソウルFZグローブ・緑 | **靈魂FZ手套・緑** | Soul FZグローブ・Green |
| 腕部防具:4745 | `Soul HSグ長袍・Green` | ソウルHSグローブ・緑 | **靈魂HS手套・緑** | Soul HSグローブ・Green |
| 腕部防具:4746 | `Soul GSグ長袍・Green` | ソウルGSグローブ・緑 | **靈魂GS手套・緑** | Soul GSグローブ・Green |
| 腕部防具:4747 | `Soul GPグ長袍・Green` | ソウルGPグローブ・緑 | **靈魂GP手套・緑** | Soul GPグローブ・Green |
| 腕部防具:4756 | `Shadow FZグ長袍White` | シャドウFZグローブ白 | **暗影FZ手套白** | Shadow FZグローブ White |
| 腕部防具:4757 | `Shadow HSグ長袍White` | シャドウHSグローブ白 | **暗影HS手套白** | Shadow HSグローブ White |
| 腕部防具:4758 | `Shadow GSグ長袍White` | シャドウGSグローブ白 | **暗影GS手套白** | Shadow GSグローブ White |
| 腕部防具:4759 | `Shadow GPグ長袍White` | シャドウGPグローブ白 | **暗影GP手套白** | Shadow GPグローブ White |
| 腕部防具:4760 | `Soul FZグ長袍・White` | ソウルFZグローブ・白 | **靈魂FZ手套・白** | Soul FZグローブ・White |
| 腕部防具:4761 | `Soul HSグ長袍・White` | ソウルHSグローブ・白 | **靈魂HS手套・白** | Soul HSグローブ・White |
| 腕部防具:4762 | `Soul GSグ長袍・White` | ソウルGSグローブ・白 | **靈魂GS手套・白** | Soul GSグローブ・White |
| 腕部防具:4763 | `Soul GPグ長袍・White` | ソウルGPグローブ・白 | **靈魂GP手套・白** | Soul GPグローブ・White |
| 腕部防具:5627 | `Blitz GFグ長袍` | ブリッツGFグローブ | **閃電GF手套** | Blitz GFグローブ |
| 腕部防具:6560 | `Truss FZグ長袍Blue` | トラスFZグローブ青 | **特拉斯FZ手套青** | Truss FZグローブ Blue |
| 腕部防具:6561 | `Truss HSグ長袍Blue` | トラスHSグローブ青 | **特拉斯HS手套青** | Truss HSグローブ Blue |
| 腕部防具:6562 | `Truss GSグ長袍Blue` | トラスGSグローブ青 | **特拉斯GS手套青** | Truss GSグローブ Blue |
| 腕部防具:6563 | `Truss GPグ長袍Blue` | トラスGPグローブ青 | **特拉斯GP手套青** | Truss GPグローブ Blue |
| 腕部防具:6568 | `Truss FZグ長袍Red` | トラスFZグローブ赤 | **特拉斯FZ手套赤** | Truss FZグローブ Red |
| 腕部防具:6569 | `Truss HSグ長袍Red` | トラスHSグローブ赤 | **特拉斯HS手套赤** | Truss HSグローブ Red |
| 腕部防具:6570 | `Truss GSグ長袍Red` | トラスGSグローブ赤 | **特拉斯GS手套赤** | Truss GSグローブ Red |
| 腕部防具:6571 | `Truss GPグ長袍Red` | トラスGPグローブ赤 | **特拉斯GP手套赤** | Truss GPグローブ Red |
| 腕部防具:6576 | `Truss FZグ長袍White` | トラスFZグローブ白 | **特拉斯FZ手套白** | Truss FZグローブ White |
| 腕部防具:6577 | `Truss HSグ長袍White` | トラスHSグローブ白 | **特拉斯HS手套白** | Truss HSグローブ White |
| 腕部防具:6578 | `Truss GSグ長袍White` | トラスGSグローブ白 | **特拉斯GS手套白** | Truss GSグローブ White |
| 腕部防具:6579 | `Truss GPグ長袍White` | トラスGPグローブ白 | **特拉斯GP手套白** | Truss GPグローブ White |
| 腕部防具:6584 | `Truss FZグ長袍Purple` | トラスFZグローブ紫 | **特拉斯FZ手套紫** | Truss FZグローブ Purple |
| 腕部防具:6585 | `Truss HSグ長袍Purple` | トラスHSグローブ紫 | **特拉斯HS手套紫** | Truss HSグローブ Purple |
| 腕部防具:6586 | `Truss GSグ長袍Purple` | トラスGSグローブ紫 | **特拉斯GS手套紫** | Truss GSグローブ Purple |
| 腕部防具:6587 | `Truss GPグ長袍Purple` | トラスGPグローブ紫 | **特拉斯GP手套紫** | Truss GPグローブ Purple |
| 腕部防具:7433 | `Brooke Fグ長袍` | ブルックＦグローブ | **布魯克F手套** | Brooke Fグローブ |
| 腕部防具:7434 | `Brooke FYグ長袍` | ブルックFYグローブ | **布魯克FY手套** | Brooke FYグローブ |
| 腕部防具:7435 | `Brooke HSグ長袍` | ブルックHSグローブ | **布魯克HS手套** | Brooke HSグローブ |
| 腕部防具:7436 | `Brooke Gグ長袍` | ブルックＧグローブ | **布魯克G手套** | Brooke Gグローブ |
| 腕部防具:7437 | `Brooke GFグ長袍` | ブルックGFグローブ | **布魯克GF手套** | Brooke GFグローブ |
| 腕部防具:7438 | `Brooke GXグ長袍` | ブルックGXグローブ | **布魯克GX手套** | Brooke GXグローブ |
| 腕部防具:8087 | `Anteka Fグ長袍` | ガウシカＦグローブ | **加烏希嘉F手套** | Anteka Fグローブ |
| 腕部防具:8088 | `Anteka FYグ長袍` | ガウシカFYグローブ | **加烏希嘉FY手套** | Anteka FYグローブ |
| 腕部防具:8089 | `Anteka HSグ長袍` | ガウシカHSグローブ | **加烏希嘉HS手套** | Anteka HSグローブ |
| 腕部防具:8090 | `Anteka Gグ長袍` | ガウシカＧグローブ | **加烏希嘉G手套** | Anteka Gグローブ |
| 腕部防具:8091 | `Anteka GFグ長袍` | ガウシカGFグローブ | **加烏希嘉GF手套** | Anteka GFグローブ |
| 腕部防具:8092 | `Anteka GXグ長袍` | ガウシカGXグローブ | **加烏希嘉GX手套** | Anteka GXグローブ |
| 腕部防具:8354 | `Blitz GXグ長袍` | ブリッツGXグローブ | **閃電GX手套** | Blitz GXグローブ |
| 腕部防具:8455 | `ル Flare ム・Blue` | ルフレアーム・青 | **露弗雷腕甲・青** | Reflet Arms・Blue |
| 腕部防具:8467 | `ル Flare ム・White` | ルフレアーム・白 | **露弗雷腕甲・白** | Reflet Arms・White |
| 腕部防具:8479 | `ル Flare ム・Red` | ルフレアーム・赤 | **露弗雷腕甲・赤** | Reflet Arms・Red |
| 腕部防具:8491 | `ル Flare ム・Black` | ルフレアーム・黒 | **露弗雷腕甲・黒** | Reflet Arms・Black |
| 腕部防具:8728 | `Gorukku Fグ長袍` | ゴルックＦグローブ | **戈魯克F手套** | Gorukku Fグローブ |
| 腕部防具:8729 | `Gorukku FYグ長袍` | ゴルックFYグローブ | **戈魯克FY手套** | Gorukku FYグローブ |
| 腕部防具:8730 | `Gorukku HSグ長袍` | ゴルックHSグローブ | **戈魯克HS手套** | Gorukku HSグローブ |
| 腕部防具:8731 | `Gorukku Gグ長袍` | ゴルックＧグローブ | **戈魯克G手套** | Gorukku Gグローブ |
| 腕部防具:8732 | `Gorukku GFグ長袍` | ゴルックGFグローブ | **戈魯克GF手套** | Gorukku GFグローブ |
| 腕部防具:8733 | `Gorukku GXグ長袍` | ゴルックGXグローブ | **戈魯克GX手套** | Gorukku GXグローブ |
| 腕部防具:9798 | `ス Flare ム` | スフレアーム | **斯弗雷腕甲** | スフレ Arms |
| 腕部防具:9845 | `Shirukku Fグ長袍` | シルックＦグローブ | **希爾克F手套** | Shirukku Fグローブ |
| 腕部防具:9846 | `Shirukku FYグ長袍` | シルックFYグローブ | **希爾克FY手套** | Shirukku FYグローブ |
| 腕部防具:9847 | `Shirukku HSグ長袍` | シルックHSグローブ | **希爾克HS手套** | Shirukku HSグローブ |
| 腕部防具:9848 | `Shirukku Gグ長袍` | シルックＧグローブ | **希爾克G手套** | Shirukku Gグローブ |
| 腕部防具:9849 | `Shirukku GFグ長袍` | シルックGFグローブ | **希爾克GF手套** | Shirukku GFグローブ |
| 腕部防具:9850 | `Shirukku GXグ長袍` | シルックGXグローブ | **希爾克GX手套** | Shirukku GXグローブ |
| 腕部防具:9859 | `Norukku Fグ長袍` | ノルックＦグローブ | **諾爾克F手套** | Norukku Fグローブ |
| 腕部防具:9860 | `Norukku FYグ長袍` | ノルックFYグローブ | **諾爾克FY手套** | Norukku FYグローブ |
| 腕部防具:9861 | `Norukku HSグ長袍` | ノルックHSグローブ | **諾爾克HS手套** | Norukku HSグローブ |
| 腕部防具:9862 | `Norukku Gグ長袍` | ノルックＧグローブ | **諾爾克G手套** | Norukku Gグローブ |
| 腕部防具:9863 | `Norukku GFグ長袍` | ノルックGFグローブ | **諾爾克GF手套** | Norukku GFグローブ |
| 腕部防具:9864 | `Norukku GXグ長袍` | ノルックGXグローブ | **諾爾克GX手套** | Norukku GXグローブ |
| 腕部防具:9941 | `Kirin Gグ長袍` | キリンＧグローブ | **麒麟G手套** | Kirin Gグローブ |
| 腕部防具:9942 | `Kirin GFグ長袍` | キリンGFグローブ | **麒麟GF手套** | Kirin GFグローブ |
| 腕部防具:9943 | `Kirin GXグ長袍` | キリンGXグローブ | **麒麟GX手套** | Kirin GXグローブ |
| 腕部防具:10650 | `Anteka Dグ長袍` | ガウシカＤグローブ | **加烏希嘉D手套** | Anteka Dグローブ |
| 腕部防具:12135 | `グ Rathian穆` | グレイアーム | **格雷腕甲** | Gray Arms |
| 腕部防具:12322 | `Brooke Dグ長袍` | ブルックＤグローブ | **布魯克D手套** | Brooke Dグローブ |
| 腕部防具:12323 | `Shirukku Dグ長袍` | シルックＤグローブ | **希爾克D手套** | Shirukku Dグローブ |
| 腕部防具:12324 | `Gorukku Dグ長袍` | ゴルックＤグローブ | **戈魯克D手套** | Gorukku Dグローブ |
| 腕部防具:12759 | `Truss Dグ長袍Blue` | トラスＤグローブ青 | **特拉斯D手套青** | Truss Dグローブ Blue |
| 腕部防具:12760 | `Truss Dグ長袍Red` | トラスＤグローブ赤 | **特拉斯D手套赤** | Truss Dグローブ Red |
| 腕部防具:12761 | `Truss Dグ長袍White` | トラスＤグローブ白 | **特拉斯D手套白** | Truss Dグローブ White |
| 腕部防具:12762 | `Truss Dグ長袍Purple` | トラスＤグローブ紫 | **特拉斯D手套紫** | Truss Dグローブ Purple |
| 腕部防具:12930 | `Norukku Dグ長袍` | ノルックＤグローブ | **諾爾克D手套** | Norukku Dグローブ |
| 腰部防具:951 | `Franc ト腰甲` | フラントコイル | **弗蘭特腰甲** | フラント Coil |
| 腰部防具:952 | `Franc トF腰甲` | フラントＦコイル | **弗蘭特F腰甲** | フラントF Coil |
| 腰部防具:1238 | `Pasu マ腰甲` | パスマコイル | **霸斯瑪腰甲** | Pasu マ Coil |
| 腰部防具:1239 | `Pasu マF腰甲` | パスマＦコイル | **霸斯瑪F腰甲** | Pasu マF Coil |
| 腰部防具:1735 | `Steno Elytra ー・Orange` | ステノアンカー・橙 | **斯特諾錨・橙** | Steno Elytra ー・Orange |
| 腰部防具:1736 | `Steno F Elytra ー・Orange` | ステノＦアンカー・橙 | **斯特諾F錨・橙** | Steno F Elytra ー・Orange |
| 腰部防具:1739 | `Steno Elytra ー・Peach` | ステノアンカー・桃 | **斯特諾錨・桃** | Steno Elytra ー・Peach |
| 腰部防具:1740 | `Steno F Elytra ー・Peach` | ステノＦアンカー・桃 | **斯特諾F錨・桃** | Steno F Elytra ー・Peach |
| 腰部防具:1743 | `Steno Elytra ー・Blue` | ステノアンカー・青 | **斯特諾錨・青** | Steno Elytra ー・Blue |
| 腰部防具:1744 | `Steno F Elytra ー・Blue` | ステノＦアンカー・青 | **斯特諾F錨・青** | Steno F Elytra ー・Blue |
| 腰部防具:1747 | `Steno Elytra ー・Red` | ステノアンカー・赤 | **斯特諾錨・赤** | Steno Elytra ー・Red |
| 腰部防具:1748 | `Steno F Elytra ー・Red` | ステノＦアンカー・赤 | **斯特諾F錨・赤** | Steno F Elytra ー・Red |
| 腰部防具:2356 | `Steno FZ Elytra ー・Orange` | ステノFZアンカー・橙 | **斯特諾FZ錨・橙** | Steno FZ Elytra ー・Orange |
| 腰部防具:2357 | `Steno FZ Elytra ー・Peach` | ステノFZアンカー・桃 | **斯特諾FZ錨・桃** | Steno FZ Elytra ー・Peach |
| 腰部防具:2358 | `Steno FZ Elytra ー・Blue` | ステノFZアンカー・青 | **斯特諾FZ錨・青** | Steno FZ Elytra ー・Blue |
| 腰部防具:2359 | `Steno FZ Elytra ー・Red` | ステノFZアンカー・赤 | **斯特諾FZ錨・赤** | Steno FZ Elytra ー・Red |
| 腰部防具:2952 | `Steno HC Elytra ー・Orange` | ステノHCアンカー・橙 | **斯特諾HC錨・橙** | Steno HC Elytra ー・Orange |
| 腰部防具:2954 | `Steno HC Elytra ー・Peach` | ステノHCアンカー・桃 | **斯特諾HC錨・桃** | Steno HC Elytra ー・Peach |
| 腰部防具:2956 | `Steno HC Elytra ー・Blue` | ステノHCアンカー・青 | **斯特諾HC錨・青** | Steno HC Elytra ー・Blue |
| 腰部防具:2958 | `Steno HC Elytra ー・Red` | ステノHCアンカー・赤 | **斯特諾HC錨・赤** | Steno HC Elytra ー・Red |
| 腰部防具:3489 | `Shell カG腰甲` | シェルカＧコイル | **謝爾嘉G腰甲** | シェルカG Coil |
| 腰部防具:3491 | `ロ Black Blos G腰甲` | ロアースＧコイル | **羅亞斯G腰甲** | ロアースG Coil |
| 腰部防具:4075 | `Steno HS Elytra ー・Orange` | ステノHSアンカー・橙 | **斯特諾HS錨・橙** | Steno HS Elytra ー・Orange |
| 腰部防具:4076 | `Steno GS Elytra ー・Orange` | ステノGSアンカー・橙 | **斯特諾GS錨・橙** | Steno GS Elytra ー・Orange |
| 腰部防具:4240 | `Steno HS Elytra ー・Peach` | ステノHSアンカー・桃 | **斯特諾HS錨・桃** | Steno HS Elytra ー・Peach |
| 腰部防具:4241 | `Steno GS Elytra ー・Peach` | ステノGSアンカー・桃 | **斯特諾GS錨・桃** | Steno GS Elytra ー・Peach |
| 腰部防具:4244 | `Steno HS Elytra ー・Blue` | ステノHSアンカー・青 | **斯特諾HS錨・青** | Steno HS Elytra ー・Blue |
| 腰部防具:4245 | `Steno GS Elytra ー・Blue` | ステノGSアンカー・青 | **斯特諾GS錨・青** | Steno GS Elytra ー・Blue |
| 腰部防具:4248 | `Steno HS Elytra ー・Red` | ステノHSアンカー・赤 | **斯特諾HS錨・赤** | Steno HS Elytra ー・Red |
| 腰部防具:4249 | `Steno GS Elytra ー・Red` | ステノGSアンカー・赤 | **斯特諾GS錨・赤** | Steno GS Elytra ー・Red |
| 腰部防具:6316 | `Steno GP Elytra ー・Orange` | ステノGPアンカー・橙 | **斯特諾GP錨・橙** | Steno GP Elytra ー・Orange |
| 腰部防具:6318 | `Steno GP Elytra ー・Peach` | ステノGPアンカー・桃 | **斯特諾GP錨・桃** | Steno GP Elytra ー・Peach |
| 腰部防具:6320 | `Steno GP Elytra ー・Blue` | ステノGPアンカー・青 | **斯特諾GP錨・青** | Steno GP Elytra ー・Blue |
| 腰部防具:6322 | `Steno GP Elytra ー・Red` | ステノGPアンカー・赤 | **斯特諾GP錨・赤** | Steno GP Elytra ー・Red |
| 腰部防具:13088 | `Steno D Elytra ー・Orange` | ステノＤアンカー・橙 | **斯特諾D錨・橙** | Steno D Elytra ー・Orange |
| 腰部防具:13089 | `Steno D Elytra ー・Peach` | ステノＤアンカー・桃 | **斯特諾D錨・桃** | Steno D Elytra ー・Peach |
| 腰部防具:13090 | `Steno D Elytra ー・Blue` | ステノＤアンカー・青 | **斯特諾D錨・青** | Steno D Elytra ー・Blue |
| 腰部防具:13091 | `Steno D Elytra ー・Red` | ステノＤアンカー・赤 | **斯特諾D錨・赤** | Steno D Elytra ー・Red |
| 脚部防具:555 | `リ Anbu茨・Blue` | リアンブーツ・青 | **莉安靴・青** | Lien Boot・Blue |
| 脚部防具:557 | `リ Anbu茨・Red` | リアンブーツ・赤 | **莉安靴・赤** | Lien Boot・Red |
| 脚部防具:559 | `リ Anbu茨・Black` | リアンブーツ・黒 | **莉安靴・黒** | Lien Boot・Black |
| 脚部防具:561 | `リ Anbu茨・White` | リアンブーツ・白 | **莉安靴・白** | Lien Boot・White |
| 脚部防具:863 | `Franc ト護腿` | フラントグリーヴ | **弗蘭特護腿** | フラント Greaves |
| 脚部防具:864 | `Franc トF護腿` | フラントＦグリーヴ | **弗蘭特F護腿** | フラントF Greaves |
| 脚部防具:1146 | `Pasu マ護腿` | パスマフット | **霸斯瑪足** | Pasu マ Feet |
| 脚部防具:1147 | `Pasu マF護腿` | パスマＦフット | **霸斯瑪F足** | Pasu マF Feet |
| 脚部防具:1396 | `マ Sharufu托` | マシャルフット | **馬沙爾足** | マ Sharufu ット |
| 脚部防具:3335 | `Shell カG護腿` | シェルカＧレッグ | **謝爾嘉G腿甲** | シェルカGレッグ |
| 脚部防具:3337 | `ロ Black Blos G護腿` | ロアースＧレッグ | **羅亞斯G腿甲** | ロアースGレッグ |
