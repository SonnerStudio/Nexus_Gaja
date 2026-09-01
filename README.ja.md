# Nexus Gaja

> *世界平和と相互理解のために*


![Nexus Gaja Logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** は、グローバル コミュニケーションに革命を起こすために設計された、インテリジェントでコンテキストに依存した通信ネットワークです。

## 目的とビジョン

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

グローバル化した世界では、言語が最大の障壁となることがよくあります。 Nexus Gaja の主な目標は、共通言語を話すかどうかに関係なく、人々の間でシームレスでバリアフリーで状況に応じて正確なコミュニケーションを可能にすることです。

それは単語を厳密に翻訳するだけではなく、**意味を伝える**ことも重要です。 Nexus Gaja は、文化的、地域的、文脈上のニュアンスを理解することで人々をより深いレベルで結びつけ、それによって本物の本物の会話を可能にします。

## 可能性と機能
- **マルチメディア通信**: システムはテキストだけでなく、画像、音声、ビデオも処理します。これにより、言語の壁を超えてリアルタイムで完全に没入型の会話 (ビデオ通話や音声メッセージなど) が可能になります。
- **文脈の敏感さ**: 従来の翻訳者によって誤解されがちな皮肉、慣用句、専門用語、地域の方言を認識します。
- **クロスプラットフォーム ネットワーク**: プライベート チャット、フォーラム スレッド (コメント付き投稿)、およびグローバル コミュニティの交流の基盤として機能します。

---

## 技術アーキテクチャ (コアコンセプト)

![Nexus Gaja 翻訳コンセプト](assets/img/nexus_translation.jpg)

Nexus Gaja の技術的中核は、厳密に 3 つの層に分割されたカスタム構築の通信モデルです。

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### コンテキストの依存関係
Nexus Gaja の翻訳では、メッセージが単独で表示されることはありません。エンジンは階層全体を考慮します。
`メッセージ` → `前のメッセージ` → `スレッドコンテキスト` → `コミュニティコンテキスト` → `言語/地域` → `ユーザー設定`

### オンデマンド翻訳による効率化
翻訳は、**リクエストに応じて** (オンデマンド) のみリソース効率よく行われます。ユーザーがコンテンツをリクエストすると、そのコンテンツは事前に設定された言語に翻訳されます。特定の言語の翻訳が生成されると、将来のリクエストを大幅に高速化するために永続的に保存 (キャッシュ) されます。

## AI 支援モデレーション (WP 1.8.4)

![Nexus Gaja AI モデレーション](assets/img/nexus_moderation.jpg)

AI 支援モデレーションにより、当社は現在の EU 規制 (第 50 条に基づく EU AI 法の透明性要件、わかりやすい正当化と異議申し立てのオプションを備えたデジタル サービス法) を考慮して、製品アイデアから技術アーキテクチャに至るまで重要な一歩を踏み出しています。

### 1. 基本原則
このアーキテクチャにとって最も重要な文は次のとおりです。 **モデレーション AI はレビュー システムであり、自律的な統治システムではありません。**
Nexus Gaja 上でどのような意見が存在できるかを自ら決定するものではなく、適度に人間を支援するように設計されています。
次の 3 つのレベルを区別します。
- **検出:** 「ここにはルール違反がある可能性があります。」
- **評価:** 「ルール違反の確率は、例えば 94% です。」
- **決定:** 「実際にどのようなアクションが取られるのか?」
3 番目のレベルは、深刻な場合には人間が制御する必要があります。

### 2. The Moderation AI as a Subsystem
Instead of a single AI, a robust subsystem is established:
```text
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  Language AI        Safety AI          Fraud AI
       │                  │                  │
       ├──────────────┬───┴──────────────┬───┤
       │              │                  │
 Translation      Behaviour          Identity
 Analysis         Analysis            Signals
       │              │                  │
       └──────────────┼──────────────────┘
                      ▼
               Risk Assessment
                      │
                      ▼
               Human Review
```

### 3. 最も重要な AI モジュール
Nexus Gaja は、次の 9 つの専門分析領域を利用します。
- **M1 – 言語理解**: 言語、方言、スラング、皮肉の指標、翻訳の問題を検出します。
- **M2 – 有害性/虐待の検出**: 侮辱、個人攻撃、嫌がらせを検出します。
- **M3 – 脅威検出**: 潜在的な脅威、脅迫、暴力のアナウンスを検出します。
- **M4 – 憎悪/非人間化の検出**: 特定の所属に基づいて人々に対する標的型攻撃を検出します。
- **M5 – スパム/操作検出**: スパム、ボットの動作、協調操作を検出します。
- **M6 – 詐欺検出**: 疑わしい詐欺行為、フィッシング、ソーシャル エンジニアリングを検出します。
- **M7 – ID の整合性**: アカウントの乗っ取り、複数のアカウント、禁止回避に関するシグナルをチェックします。
- **M8 – メディアの安全性**: 画像、音声、ビデオ、ドキュメントを分析します。
- **M9 – コンテキスト エンジン**: 最も重要なモジュール。個々の調査結果を統合します。

### 4. コンテキスト エンジンが重要な理由
純粋なキーワード検索だけでは不十分です。 「笑いすぎて彼を殺すことができた」は意味的には暴力を含んでいますが、表現です。 「明日の午後8時に彼の家の前で撃ってやる」というのは状況が全く違う。 AI は、そのステートメントが特定のコンテキストで何を意味するのかを理解する必要があります。

### 5. 多言語モデレーション
モデレーションは単純に言葉を比較することはできません。意味レベル (ドイツ語の慣用句、日本語の慣用句、地域の表現など) を分析する必要があります。

### 6. 原語 + 翻訳
原文と翻訳は別々に分析されます。その場合にのみ、「複合モデレーション評価」が行われます。これにより、Nexus Gaja は、翻訳自体が事実をエスカレートしたり変更したりした可能性があるかどうかを判断できます。

### 7. 信頼スコア
すべての AI 評価には信頼度スコアが付けられます (例: 脅威確率: 0.96)。ただし: **信頼スコア ≠ 真実** スコア 96% は、モデルの分類の確実性が高いことを意味するだけであり、必ずしもユーザーが有罪であることを意味するわけではありません。

### 8. Uncertainty Becomes a Signal Itself
If the AI is uncertain (e.g., Threat: 0.62, Satire: 0.54), it must not simply enforce harsh rules. Instead, uncertainty is built directly into the architecture: **Human Review Required**.

### 9. 4 つの決定ゾーン
- 🟢 **緑**: 準拠している可能性が高くなります。 →アクションなし。
- 🟡 **黄色**: 違反の可能性があります。 → 監視し、必要に応じて警告を発します。
- 🟠 **オレンジ**: 違反の可能性があります。 →モデレーションレビュー。
- 🔴 **赤色**: 重大な違反の可能性があります。 → 即時保護措置 + 人による審査。

### 10. 「AI 罰」はありません
**AI は最終的な制裁を課しません。** 深刻なセキュリティ上の懸念に対して、技術的な即時措置 (メッセージを一時的に保留するなど) を引き起こす可能性がありますが、最終的な決定は検証可能です。

### 11. 保護措置は自動的に行われる可能性があります
具体的な脅威が発生した場合（脅威の検出→信頼性が高い→一時的な制限→人間によるレビュー→決定）、AIを判断者にさせることなく、脅威にさらされたユーザーを保護します。

### 12. AI はその決定を正当化できなければなりません
DSA には明確かつ具体的な理由が必要です。 AI は構造化された推論を提供します: ルール (NG-CONDUCT-004)、検出 (潜在的な具体的な脅威)、信頼度 (0.94)、関連するコンテキスト (過去 4 つのメッセージ)、推奨アクション (人間によるレビュー)。

### 13. AI はコンテンツを密かに変更してはなりません
**モデレーション AI は、気付かれずに元のコンテンツを変更してはなりません。** 自動修正、翻訳、または要約中、オリジナルは常に保存されます。

### 14. AI 生成コンテンツ
私たちは、人間が作成したもの、AI が支援したもの、AI が生成したもの、AI が操作したものを区別します。これはコンテンツのメタデータの一部になります。

### 15. AI コンテンツと AI 出所レイヤーのラベル付け
EU AI 法 (2026 年 8 月発効) の透明性規則によれば、AI によって生成されたコンテンツは識別可能でなければなりません。メタデータ (AI-Origin、Model、Timestamp、Human Review) を保存する AI Provenance Layer を提供します。

### 16. ディープフェイクの検出
このアーキテクチャは、合成画像、クローン音声、ディープフェイクを検出することを目的としています。ただし、検出は自動的に証明されるわけではありません。

### 17. 自動「真実機械」は存在しない (節度 ≠ 事実確認)
あるシステムは「コンテンツがルールに違反していないか？」をチェックします。 (コンテンツモデレーション)、別の情報では、「どのような情報とソースが利用可能ですか?」が提供されます。 （情報支援）。意見は単に「間違っている」という理由で削除されるわけではありません。

### 18. 文化的誤解からの保護
AI には、一国のコミュニケーション規範が世界標準として想定されるのを防ぐために **文化的コンテキスト モデル** が必要です。

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. 単一の AI スコアに基づく罰はない
単一の自動分類結果 (テキスト + コンテキスト + 行動 + 言語 + メディア + ルール エンジン = リスク評価) のみに基づいて、厳格な調整介入を行うことはできません。

### 21. ユーザー行動のシグナルと社会信用システムの不在
これは、一般的な社会的評価システムではなく、技術的な不正行為のシグナル (大量のスパム投稿など) に関連しています。 Nexus Gaja は社会信用システムを維持していません。節度は個人の価値の評価ではなく、安全を確保するものです。

### 22. モデレーション AI は監査可能でなければなりません
トレーサビリティを確保するために、関連するすべての自動決定がログに記録されます (イベント ID、ルール ID、信頼性、人間によるレビューなど)。

### 23. 偽陽性、偽陰性、品質指標
エラーの種類が監視されます。ダッシュボードは、適合率、再現率、特に **異議申し立て撤回率** (成功した申し立ての数) を測定します。

### 24. 言語の公平性と翻訳のバイアス
モデレーションの品質は、サポートされているすべての言語で同等である必要があります (多言語モデレーション ベンチマーク)。モデレーションの結果がオリジナルと翻訳の間で異なる場合 (翻訳の競合)、これを特にレビューする必要があります。

### 25. アーキテクチャ提案およびポリシー エンジン
ルール (ポリシー エンジン) は AI モデルにハードコーディングされません。 AI は調査結果を提供します。ポリシー エンジンは現在のルールに基づいて決定します。これにより、**ルールを変更せずにモデルを変更**できます。

### 26. 最終的な権威は人間のまま
- **NG-AI-MOD-001**: AI は検出と分類を支援しますが、重大な決定において人間によるレビューに代わるものではありません。
- **NG-AI-MOD-002**: 自動モデレーションの決定は追跡可能、ログ可能、検証可能である必要があります。

**概要**: 私たちは、AI 検出、コンテキストとリスク分析、ポリシー エンジン、ヒューマン ガバナンスの 4 段階のシステムを構築しています。これにより、危険な「判断者としての AI」アーキテクチャを作成することなく、強力な自動化が可能になります。

## 資金調達の原則と収益モデル (WP 1.10.1)

![Nexus Gaja 財務モデル](assets/img/nexus_finance.jpg)

Nexus Gaja には、**プラットフォーム内に従来の広告を掲載しない**という非常に重要な経済原則が適用されます。
これは、Nexus Gaja を今日の多くのソーシャル ネットワークと根本的に区別するものです。ただし、これは Nexus Gaja が商業的な性格を持つことができないという意味ではありません。それどころか、プラットフォームは社会的目的を持続できるように経済的に実行可能でなければなりません。経済活動は目的を達成するための手段であり、プラットフォームの主な目的ではありません。

### 1. 原則 NG-FIN-001
Nexus Gaja は、ユーザーの関心や個人データの収益化を通じてではなく、ユーザーの利益とは切り離された透明な収益源を通じて運営資金を調達しています。

### 2. 従来の広告は禁止
具体的に禁止されているのは次のとおりです。
- バナー広告
- ポップアップ広告
- 自動再生動画広告
- 標準フィードのスポンサー付き投稿
- パーソナライズされた広告プロファイル
- ユーザープロフィールまたは個人データの販売
- 個人的な会話から派生した広告。

Nexus Gaja は、**広告スペースではなくコミュニケーション スペース**であり続けます。

### 3. 広告なしの資金調達 (6 本の柱)
資金調達は 6 つの柱に基づいて構築されています。
```テキスト
                 ネクサスガジャ
                     │
       ┌─────────┼─────────┐
       ▼ ▼ ▼
   プレミアム団体への寄付
       │ │ │
       §───────┼─────────┤
       ▼ ▼ ▼
    助成金パートナーシップサービス
「」

#### Pillar 1 – Free Basic Membership
**Nexus Gaja Free** enables basic international understanding for everyone (profile, international communication, posts, communities, chats, basic translation) at no cost.

#### 第 2 の柱 – プレミアム製品
任意の有料サービス (**Nexus Gaja Plus**) は、より大きなストレージ制限、より高いメディア品質、拡張された AI クォータ、および組織機能を提供します。
**重要 (ダーク フリーミアムではなくフリーミアム):** 基本的なコミュニケーションを人為的に低下させてはなりません。

#### 柱 3 – 組織
学校、大学、NGO、企業、自治体向けの特別アカウント (**Nexus Gaja Organization**)。学校は、国際理解の乗数として制度的な料金で支援を受けることができます。

#### 第 4 の柱 – 寄付
**Nexus Gaja Funding Pool** は、一般寄付および指定された寄付 (例: 「国際的な青少年コミュニケーションのため」) を受け付けています。 **資金配分台帳**により、資金の透明性のある配分が保証されます。
**目的基金とトンボラ:** 寄付金の一部は、無料または割引で使用できるプールに供給されます。宝くじ/トンボラのメカニズムにより、これらの資金を透明かつ監査可能に割り当てることができます。

#### 第 5 の柱 – 機関投資家への資金提供
財団、文化資金プログラム、または州のプログラム。
**NG-FIN-002:** 財政的支援によって編集または技術的管理が行われることはありません (独立性)。

#### 第 6 の柱 – 商用サービス
**Translation-as-a-Service** (API)、組織コミュニケーション、国際会議室などの B2B サービスを、標準のユーザー フィードに負担をかけずに実現します。

### 4. データ収益化と監視経済の不在
**NG-FIN-003:** ユーザーの個人データは商品ではありません。リスト、プロフィール、履歴の販売は禁止されています。 Nexus Gaja は心理監視 (監視経済) から利益を得ているわけではありません。

### 5. 財務の透明性と資金台帳
**Nexus Gaja の財務の透明性:** 集約された財務構造の公開。指定された寄付は技術的な会計処理を受けます (基金 ID → 目的 → 残高 → 配分)。社会的目的を企業マーケティングに相互補助することはありません。

### 6. 連帯に基づく資金調達モデル
価格設定はコスト重視、公平性、連帯感に基づいています。
**連帯プレミアム:** プレミアム ユーザーが別のユーザーのアクセスの一部に資金を提供するための任意のオプション。強制的な連帯やプレミアムクラス社会（無料ユーザーに対する敬意や節度の低下）は固く禁止されています。

### 7. エンゲージメント エコノミーの代わりに経済的な KPI
ユーザーを「可能な限り長く」オンラインに保つことに依存する必要はありません (怒り餌や無限のフィードはありません)。
代わりに、次のような指標を使用します。
- **グローバル コミュニケーション インデックス (GCI):** 異なる言語/文化地域の人々の間で成功したコミュニケーション関係。
- **プラットフォーム持続可能性比率 (PSR):** 経常収益 / 経常運営コスト (目標 ≥ 1)。

### 8. 明示的に望まないこと (ネガティブ リスト)
Nexus Gaja は以下から資金提供を受けていません**。
❌ 個人データの販売
❌ パーソナライズされた従来の広告
❌ 広告目的でのユーザー行動の監視
❌私的な通信データの販売
❌ 隠された AI データの使用
❌ 操作的なプレミアムペイウォール
❌ 収益化のための人為的なリーチ制限
❌ 政治的影響力を得る
❌ 特権的なモデレーション決定の購入。

### 9. 予備的な財務アーキテクチャ
```テキスト
                         ネクサスガジャ
                              │
             ┌───────┼───────┐
             │ │ │
             ▼ ▼ ▼
          ユーザー組織 企業
             │ │ │
             ━━━━━━━━━━━━━━━━━━┘
                              │
                       プラットフォームサービス
                              │
          ┌───────────┼───────────┐
          ▼ ▼ ▼
       プレミアム寄付 API
                              │
                    ┌─────┴─────┐
                    ▼ ▼
               一般資金制限資金
                                        │
                                        ▼
                                  社会的目的
「」

### Summary of Financing Principles (NG-FIN)
- **NG-FIN-001:** No financing through traditional advertising.
- **NG-FIN-002:** No editorial/technical control through financial support.
- **NG-FIN-003:** Personal data is not a commodity.
- **NG-FIN-004:** Basic communication remains accessible without payment.
- **NG-FIN-005:** Premium offerings must not degrade free users.
- **NG-FIN-006:** Earmarked funds are managed according to their purpose.
- **NG-FIN-007:** Transparent management of donations and grants.
- **NG-FIN-008:** Commercial B2B services do not compromise independence.
- **NG-FIN-009:** Focus on sustainability rather than maximum monetization.
- **NG-FIN-010:** The structure permanently secures the social purpose.

## API、インターフェイス、および通信アーキテクチャ (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### Core Principles
- **No Direct Database Access:** Components communicate exclusively via defined interfaces (APIs or Events), never through direct database queries of other services.
- **API Gateway:** All external client requests route through an API Gateway handling authentication, routing, and rate limiting.
- **Provider Abstraction:** External services (AI models, payment providers, translation engines) are integrated via abstraction layers, avoiding hardcoded dependencies and enabling flexible provider swapping.

### コミュニケーションパターン
- **同期 API (REST/HTTPS):** ログイン、プロファイル設定、直接翻訳などの即時リクエストに使用されます。
- **非同期イベント (イベント バス):** 遅延された分離された処理のための Nexus Gaja の中枢神経系 (例: モデレーション、翻訳、および通知を非同期にトリガーする `Message.Created`)。
- **リアルタイム (WebSocket):** ライブ チャットとタイピング インジケーターの専用チャネル。

### Security and Reliability
- **Zero-Trust Model:** Internal network traffic is not automatically trusted; sensitive service-to-service communication requires authentication.
- **Idempotency & Outbox Pattern:** Critical operations (like donations or messaging) are designed to be idempotent to prevent duplicate processing, utilizing the Outbox pattern to ensure events are never lost even during database transactions.

## MVP ドメイン モデル (WP 1.12)

![Nexus Gaja モジュラー モノリス](assets/img/nexus_architecture.jpg)

Nexus Gaja は、明確なドメイン境界を持つモジュール式モノリスとして設計された、厳密にドメイン駆動型の MVP アーキテクチャ (ADR-025) を採用しています。この構造は、後で特定のドメインを分割する柔軟性を維持しながら、マイクロサービスの早期の複雑化を防ぎます。

### コアドメインエンティティ
このアーキテクチャでは、データの整合性を確保し、「ユーザー名 = 人間」のような構造的な落とし穴を回避するために、明確に異なる概念が分離されています。
- **アイデンティティとアカウント:** 「個人」≠「ユーザーアカウント」≠「本人確認」。認証された個人はアカウントを介して参加しますが、エンティティは分離されたままになります。
- **コミュニケーション:** `メッセージ` ≠ `翻訳`。元のメッセージは不変のままです。翻訳はリンクされたエンティティです。
- **モデレーション:** 「報告」≠「モデレーションの決定」。報告書は単なる主張にすぎません。モデレートケースが調査を実施します。
- **財政:** `寄付` ≠ `基金残高`。支払いは不変の台帳を介して基金に記録され、財務の透明性が確保されます。

### 相互接続されたドメイン
このシステムは、アイデンティティ、アカウント、組織、コミュニケーション、コミュニティ、言語、モデレーション、通知、財務、ガバナンスという明確な論理ドメイン (境界コンテキスト) に分割されています。これらのドメインは、現実世界のエンティティ (ユーザー、学校、NGO) からデジタル インタラクションおよび関連するガバナンスまでの過程全体をマッピングします。

## プロジェクトのステータス
このプロジェクトは現在、アクティブなアーキテクチャと計画段階にあります。
現在進行中のアーキテクチャ上の決定は、「/docs」フォルダーに文書化されています。---

## ライセンスと知的財産権

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — 全ての権利を保有。**

**Nexus Gaja** は、**SonnerStudio** として活動する **Jan Friske** の独占的な知的財産です。

Jan Friske は、すべての概念、アーキテクチャ、ドメインモデル、ブランドアイデンティティ、および関連ドキュメントを含む Nexus Gaja の唯一の創造者、設計者、および所有者です。

**いかなる第三者にも権利、ライセンス、または所有権は付与されません**（テクノロジー業界での規模、市場での地位、または影響力にかかわらず）。

### 明示的な書面による同意なしに許可されていないこと:
- ❌ このソフトウェアまたはそのドキュメントのコピー、複製、または配布
- ❌ 修正、改変、または派生物の作成
- ❌ Nexus Gaja のいかなる部分の商業的使用
- ❌ このリポジトリのコンテンツを AI または LLM システムのトレーニングデータとして使用
- ❌ 第三者へのサブライセンスまたは権利の譲渡

### 連絡先
ライセンスに関するお問い合わせ: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*「Nexus Gaja」および Nexus Gaja ロゴは Jan Friske の商標です。名前またはブランドの無断使用は禁止されています。*

➡️ 完全なライセンス条項は [LICENSE](LICENSE) ファイルをご覧ください
