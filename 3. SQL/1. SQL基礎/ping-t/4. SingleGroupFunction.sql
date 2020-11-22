ADD_MONTHS(date, integer)

-- 日付dateに月数integerを加えて戻します。
-- dateが月の最終日の場合、または結果の月の日数がdateの日付コンポーネントよりも少ない場合、戻される値は結果の月の最終日となります。それ以外の場合、結果にはdateと同じ日付コンポーネントが含まれます。

SUBSTR(char, position[, substring_length])

-- charのpositionの文字からsubstring_length文字分の文字列を抜き出して戻します。

INSTR(string, substring[, position, occurrence])

-- stringのsubstringを検索します。
-- positionは、Oracle Databaseが検索を開始するstringの文字の位置を示す0(ゼロ)以外の整数です。
-- occurrenceは、stringの中で何番目に現れるsubstringを検索するかを示す整数です。
-- INSTR関数では英文字の大文字と小文字は区別されます。

INITCAP(char)

-- INITCAPは、各単語の最初の文字を大文字、残りの文字を小文字にしてcharを戻します。
-- 単語は空白または英数字以外の文字で区切ります。
-- 戻り値は、charと同じデータ型です。

TRIM( [LEADING | TRAILING |  BOTH ,] trim_character, FROM trim_source) 
TRIM(trim_source)

-- TRIMによって、文字列の先行または後続文字(またはその両方)を切り捨てることができます。
-- BOTHを指定するか、またはいずれも指定しない場合、Oracleはtrim_characterと等しい先行および後続文字を削除します。
-- trim_characterを指定しないと、デフォルト値は空白になります。
-- trim_sourceのみを指定すると、Oracleは先行および後続空白を削除します。
-- 削除文字には任意の1文字を指定できますが、文字列は指定できません。

LPAD(expr1, n, expr2)
RPAD(expr1, n, expr2)

-- L(R)PADは、expr1の左(右)側にexpr2に指定した文字を連続的に埋め込んでn桁にして戻します。
-- expr1はNULL以外である必要があります。expr2を指定しない場合、デフォルトで空白1個が指定されます。
-- expr1およびexpr2は、CHAR、VARCHAR2、NCHAR、NVARCHAR2、CLOBまたはNCLOBデータ型です。
-- expr1がnより長い場合、このファンクションはnに収まるexpr1の一部を戻します。

CONCAT(char1, char2)

-- CONCATは、char2に連結されているchar1を戻します。
-- このファンクションは、連結演算子(||)と同等です。

LAST_DAY(date)

-- LAST_DAYは、dateを含む月の最終日の日付を戻します。

NEXT_DAY(date, char)

-- charで指定した曜日で、日付dateより後の最初の日付を戻します。
-- 戻り型は、dateのデータ型に関係なく常にDATEです。
-- 引数charは、セッションの日付言語での曜日である必要があります(フルネームでも省略形でも可)。

REPLACE(char, search_string[, replacement_string])

-- REPLACEは、replacement_stringですべてのsearch_stringを変換してcharを戻します。
-- replacement_stringを指定しない場合またはNULLの場合、すべてのsearch_stringが削除されます。
-- search_stringがNULLの場合、charが戻されます。

MONTHS_BETWEEN(date1, date2)

-- 日付date1とdate2の間の月数を戻します。
-- 月および月の最終日は、パラメータNLS_CALENDARによって定義されます。
-- date1がdate2より後の日付の場合、結果は正の値になります。date1がdate2より前の日付の場合、結果は負の値になります。
-- date1およびdate2が、月の同じ日または月の最終日の場合、結果は常に整数になります。