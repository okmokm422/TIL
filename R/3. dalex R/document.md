# Dalexのまとめ

# 1. 理論編（岡）

- [Explanatory Model Analysis Explore, Explain and Examine Predictive Models](https://pbiecek.github.io/ema/)より

## 1-1. インスタンスレベル

### BreakDown

- 説明変数に条件をつけることで、説明変数 𝑥 のモデル 𝑓(𝑥) による予測への貢献度合いを計算する。

- $v(j, x_*)$を$j$番目の説明変数、instance $x_*$（titanicでいうと乗客$x_*$さん）に対する予測値とすると、

    $v(j, x_*) = E_X[f(X) | X^1 = x^1_*, \ldots, X^j = x^j_*] - E_X[f(X) | X^1 = x^1_*, \ldots, X^{j-1} = x^{j-1}_*]$
    
    - $j$番目の説明変数の貢献度合いは、  
    （$j$番目まで説明変数の入力があったときの$f(X)$の期待値）ー（$j-1$番目まで説明変数の入力があったときの$f(X)$期待値）
    といえる。  
    - つまり、j番目に入力した説明変数によってどの程度期待値が変わったか？を表す。

### CeterisParibus

- Ceteris-paribus (CP) profilesとは  
    注目する説明変数以外の説明変数の値を固定したときの期待値について調べる。
    他の値を固定したとき、注目する説明変数の値を変化させることで、その説明変数へのモデルへの影響度を図る。
    各説明変数がモデル応答にどう影響を与えるかを調べるためには、各説明変数の曲率を調べる。 


### SHAP

- SHAPはゲーム理論のShapley valueをモデルにしている。

- BDPlotの順序の依存性を解決するため、すべての順序について貢献度を調べてその平均を取ったもの。

- Shapley value  
    $\displaystyle \varphi(x_*,j) = \frac{1}{p!} \sum_{J} \Delta^{j|\pi(J,j)}(x_*)$
    
    - $\varphi(x_*,j)$：すべての説明変数の重要度の平均値
    - $\pi(J,j)$：$j$番目の変数より前に位置する、$J$説明変数のセット
    - $p!$：説明変数の集合が取りうる順列

## データセットレベル

### model performance


### VariableImportance

- 説明変数やそのグループが取り除かれたとき、モデルのパフォーマンスがどの程度変化するのかを調べる。


-  考え方
    【前提】  
    - $p$個の説明変数の$n$件の観測データについて考える。  
    - $\widetilde{y}=(f(x_1),\ldots,f(x_n))$：モデル$f()$の集合  
    - $\mathcal L(\widetilde{y}, y)$：元のデータによる損失関数。尤度。  
  
    【計算方法】  
    1. 元のデータで損失関数$L = \mathcal L(\widetilde{y}, y)$を計算する。  
    2. データをリサンプリングしたり、置き換えたりしたときの損失関数を計算する。  
        （ここでサンプリングによるランダム性が出るので注意！）
    3. 元のモデルの損失関数と、２の損失関数の差を計算し、正規化。  

### AggregatedProfiles

# 2. コード解析

## 2-1. インスタンスレベル（飯倉さん）


## 2-2. データセットレベル（八巻さん）

---
### Explainer.model_performance
Explainerオブジェクトのメソッドmodel_performanceを実行すると、ModelPerformanceオブジェクトが作られる。

#### Explainer.**model_performance**(self, model_type=model_type, cutoff=cutoff)
- 各種スコアを計算し、モデルの性能指標を表示する。

#### 引数
- **model_type**: {'regression', 'classification'}, default=None\
Explainerオブジェクト作成時に指定していない場合は指定が必須。モデルの予測種類を指定。回帰なら'regression'、分類なら'classification'。

- **cutoff**: float, \[0, 1\], default=0.5 \
model_type='classification'の場合に、予測の閾値を指定する。

#### リターン
- **ModelPerformance**オブジェクト

#### インスタンス変数
- **results**: DataFrame
全てのpermutation結果を平均した値を格納するDataFrame。 \
model_type='regression'なら'rme', 'rmse', 'r2', 'mae', 'mad'の値が格納される。 \
model_type='classification'なら'recall', 'precision', 'f1', 'accuracy', 'auc'の値が格納される。

- **permutation**: DataFrame \
全てのpermutation結果の値を格納するDataFrame(keep_raw_permutations=Trueの場合)。

#### メソッド
**plot**(self, objects=None, title="Reverse cumulative distribution of |residual|", show=False):
- 予測値の真の値に対する誤差の、逆累積プロットを表示。

**引数**
- **objects**: ModelPerformanceオブジェクトもしくはそれらのlistかtuple, default=None \
同一グラフにプロットして比較するVariableImportanceオブジェクト

- **title**: str, default='Reverse cumulative distribution of |residual|' \
グラフタイトル。

- **show**: bool, default=False \
Trueの場合はグラフを表示。Falseの場合はグラフオブジェクトを返す。

---

### Explainer.model_parts
Explainerオブジェクトのメソッドmodel_partsを実行すると、VariableImportanceオブジェクトが作られる。

#### Explainer.**model_parts**(self, loss_function=None, type='variable_importance', N=1000, B=10, keep_raw_permutations=True, variables=None, variable_groups=None, processes=1, random_state=None):
- ある特徴量をランダムに並び替えた時の誤差の増減を見ることで、特徴量の重要度を測定する(permutation importance)。

#### 引数
- **loss_function**: {'rmse', 'mse', 'mae', 'mad', 'r2', '1-auc'}, default=None \
特徴量の重要度を評価するための関数を指定。Noneの場合、Explainerにおいて`model_type='regression'`なら`'rmse'`が、`classification`なら`1-auc`が内部的に割り当てられる。

- **type**: {'variable_importance', 'ratio', 'difference'}, default='variable_importance' \
特徴量重要度の表示方法を指定。指定した評価関数値の平均値(`variable_importance`)、差の比率(`ratio`)、差(`difference`)から選択可能。

- **N**: int, default=1000 \
特徴量の重要度計算に使用するレコード数。Noneの場合、explainerに渡されたデータセット全てを使用する。

- **B**: int, default=10 \
permutation試行回数。重要度は各回の結果の平均を取ったものとなる。

- **variables**: list, ndarray or dict, default=None \
重要度を計算する特徴量を選択。Noneの場合、全特徴量が選択される。 \
variable_groupsがNoneでない場合、無視される。

- **variable_groups**: dict, default=None \
特徴量のリストを格納した辞書。いくつかの特徴量を集約して重要度を見る時に使用する。

- **processes**: int, default=1\
並行して計算するプロセス数。上限は環境のCPU数。

- **random_state**: int, default=None \
ランダムシードの指定。

- **keep_raw_permutations**: bool, default=True \
Trueを指定すると、permutationした各回の結果がself.permutationに格納される。

#### リターン
- VariableImportanceオブジェクト

#### インスタンス変数
- **results**: DataFrame
全てのpermutation結果を平均した値を格納するDataFrame。 \
特徴量ごとの結果に加え、元のデータセットのスコア(\_full_model_)と全ての特徴量をランダムに並び替えた時のスコア(\_baseline_)が格納されている。

- **permutation**: DataFrame \
全てのpermutation結果の値を格納するDataFrame(keep_raw_permutations=Trueの場合)。

#### メソッド
**plot**(self, objects=None, max_vars=10, digits=3, rounding_function=np.around, bar_width=16, \
split=("model", "variable"), title="Variable Importance", vertical_spacing=None, show=True)

- permutation importanceの結果をグラフに表示する。

**引数**
- **objects**: VariableImportanceオブジェクトもしくはそれらのlistかtuple, default=None \
同一グラフにプロットして比較するVariableImportanceオブジェクト

- **max_vars**: int, default=10 \
それぞれのモデルについてのプロット数。

- **digits**: int, default=3 \
グラフに表示される特徴量重要度の桁数。

- **rounding_function**: function, default=np.around \
グラフに表示される特徴量重要度の丸め関数。

- **bar_width**: int, default=16 \
棒グラフの幅を指定。

- **split**: {'model', 'variable'}, default='variable' \
プロットの分割方法を指定。'model'の時はモデル別、'variables'の時は特徴量別にプロットする。

- **title**: str, default='Variable Importance' \
グラフタイトル。

- **vertical_spacing**: float, \[0, 1\], default=None \
棒グラフの幅に対する間隔の比。Noneの場合は 0.2/{プロット数} となる。

- **show**: bool, default=True \
Trueの場合はグラフを表示。Falseの場合はグラフオブジェクトを返す。

---

### Explainer.model_profile
Explainerオブジェクトのメソッドmodel_profileを実行すると、AggregatedProfilesオブジェクトが作られる。

#### Explainer.**model_profile**(self, type='partial', N=300, variables=None, variable_type='numerical', groups=None, span=0.25, grid_points=101, center=True, processes=1, random_state=None, verbose=True)
- 特徴量毎に、値の変化の予測値への寄与を計算、可視化する。

#### 引数
- **type**: {partial, conditional, accumulated}, default='partial' \
寄与の計算方法を指定。'partial'はデータセット全体での単純平均、その他は重みづけ平均。

- **N**: int, default=300 \
寄与の計算に使用するレコードの個数。explainerに渡されたデータセットの行番号順にサンプリングされる。

- **variables**: str, list, numpy.ndarray or pandas.Series, default=None \
寄与を計算する特徴量を選択。Noneの場合、全ての特徴量について計算される。

- **variable_type**: {'numerical', 'categorical'}, default='numerical' \
寄与を計算する特徴量のタイプを選択。'numerical'なら数値変数、'categorical'ならカテゴリ変数について計算される。 \
(注: 文字列型の列をカテゴリ変数、それ以外を数値変数と見做すので、数値型で格納されているカテゴリ変数などの取り扱いに注意が必要。)

- **groups**: str, list, numpy.ndarray or pandas.Series, default=None \
カテゴリ変数を表す列名を渡すと、その列に存在するカテゴリ毎に他の特徴量の寄与が計算される。  \
listなどで複数の列名を指定すると、各列のカテゴリ全ての組み合わせ毎に他の寄与が計算される。

- **span**: float, default=0.25 \
重みづけに使用されるガウシアンフィルタの係数。値が大きいほど平坦な重みづけに(単純平均に近く)なる。

- **grid_points**: int, default=101 \
寄与の計算時の、数値データの分割数。

- **center**: bool, default=True \
Falseのとき、寄与の平均が0になるよう計算される。

- **processes**: int, default=None \
並行して計算するプロセス数。上限は環境のCPU数。

- **random_state**: int, default=None \
ランダムシードの指定。

- **verbose**: bool, default=True \
計算の進行状況を示すかどうかを選択。

#### インスタンス変数
- **results**: DataFrame \
全てのデータに関するCeteris Paribusの結果を列挙して格納するDataFrame。

#### メソッド
**plot**(self, objects=None, geom="aggregates", variables=None, size=2, alpha=1, facet_ncol=2, title="Aggregated Profiles", title_x="prediction", horizontal_spacing=0.05, vertical_spacing=None, show=True)

- 寄与の計算結果をグラフに表示。variable_type='numerical'の時は折れ線グラフ、variable_type='categorical'の時は棒グラフで表示する。

**引数**
- **objects**: AggregatedProfilesオブジェクトもしくはそれらのlistかtuple, default=None \
同一グラフにプロットして比較するAggregatedProfilesオブジェクト

- **geom**: {"aggregates", "profiles"}, default="aggregates" \
"profiles"とすると、各レコードについてのCPの結果を全てプロットする。

- **variables**: str or list, default=None \
結果を表示する特徴量を指定。表示可能な特徴量と1つも被っていないとエラーになるが、誤った特徴量列名が存在しても他が一つでも合っていればエラーにならない。

- **size**: float, default=2 \
折れ線グラフの幅を指定。

- **alpha**: float, [0,1], default=1 \
プロットの透過度を指定。

- **facet_ncol**: int, default=2 \
１行に表示するグラフの数を指定。

- **title**: str, default='Aggregated Profiles' \
グラフタイトル。

- **title_x**: str, default='Prediction' \
縦軸のタイトル。

- **horizontal_spacing**: float, default=0.1 \
プロットエリア間の横方向の間隔を、プロットエリアの幅に対する比で指定。

- **vertical_spacing**: float, default=None \
プロットエリア間の縦方向の間隔を、プロットエリアの高さに対する比で指定。

- **show**: bool, default=True \
Trueの場合はグラフを表示。Falseの場合はグラフオブジェクトを返す。


# 3. チュートリアル

## 3-1. Python

### 3-1-1. 分類（足立さん）

### 3-1-2. 回帰（上田さん）

## 3-2. R

### 3-2-1. 分類（岡）

### 3-2-2. 回帰（岡）