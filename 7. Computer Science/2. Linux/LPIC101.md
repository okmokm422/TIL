# 参考

 - [Linux - System Hardware](https://www.infraeye.com/study/linuxz1.html)

# 基本用語
|用語|意味|
|:---|:---|
|BIOS（Basic I/O System）|最もハードウェアに近い部分を司るシステム。<br>マザーボードや拡張カードに搭載されたフラッシュROMに書き込まれている。<br>【機能】<br>1. 記憶装置（HDD）等に対する最低限の認識<br>2. デバイスのブート用の特殊領域（MBR）を読み込み<br>3. ブートローダに制御を移す<br>【設定可能項目】<br>・日付と時刻<br>・電源管理<br>・起動デバイスの優先順位<br>・組み込みデバイスの有効/無効化|
|UEFI(Unified Extensible Firmware Interface)|・IntelがBIOS（Basic I/O System）を置き換えるために考案したEFIの統一仕様<br>・GUIでの操作をサポート<br>・ESP（EFIシステムパーティション）（UEFIシステムにおいて、物理的なマシンを起動し、ファームウエアが読み込まれた後、その後の起動シーケンスで最初にアクセスされる領域）は/boot/efiにマウントされる<br>・GPT（GUID Partition Table）というパーティション形式のHDDからの起動に対応しており、3TB以上のHDDからの起動をサポートしている。<br>|
|カーネルモジュール|カーネルで組み込まれる機能のプログラム部品。カーネルから独立している。|
|I/Oポートアドレス|周辺機器(デバイス)とCPUがデータをやり取りする際に使用する16ビットのアドレス|
|SCSIデバイス（スカジー）|コンピュータと周辺機器を接続するためのインターフェイス|
|D-Bus（Desktop Bus）|プログラム同士が情報を伝達するプロセス間通信機構|
|TA(ターミナルアダプタ)|データをISDN回線の中を通れる形に変換する機器|
|ホットプラグデバイス|電源を入れたままの接続・取り外しに対応。プラグアンドプレイデバイスともいう。|
|コールドプラグデバイス|システムが停止している状態でのみデバイスの差し替えができるデバイス。|
|DMA|CPUを介さずに周辺機器やメインメモリ（RAM）などの間で直接データ転送を行う方式|
|DMAチャネル|DMA転送で使う通信経路|
|SATAインターフェース|HDDの仕様規格で主流なもの。単線で連続（シリアル）転送。|
|ACPI（Advanced Configuration and Power Interface）|コンピュータの電源管理や構成に関する規格 <br>OS上でシャットダウンや再起動などを行う際の命令は、ACPIイベントとして通知される<br>|
|acpidデーモン|ACPIイベントを監視し、イベントに対応する処理を実行|

<br>
<br>

# コマンド
|コマンド|意味|同義|
|:---|:---|:---|
|dmesg|システム起動時に出力されたメッセージを確認|journalctl --dmesg/journalctl -k|
|dmesg --clear|手動でリングバッファ（一時的にデータを溜めておく記憶場所）の内容をクリアする。rootユーザで実行。|
|modprobe|依存関係を考慮してカーネルモジュールをロードまたはアンロード|
|lsmod|ロードされているカーネルモジュールの情報|cat /proc/modules|
|lsusb|接続されたUSBデバイスの情報を表示|cat /proc/bus/usb/devices|
|lscpu|CPUの情報を表示|cat /proc/cpu|
|lspci|PCIデバイスの情報を表示<br>・PCI識別番号<br>・PCIデバイスの種類<br>・ベンダー名（ベンダーID）<br>・デバイス名<br>・バスの速度<br>・IRQ番号<br>・I/Oポートアドレス|cat /proc/bus/pci/devices|
|journalctl --dmesg|systemdが管理するシステム起動時に出力されたメッセージを確認|dmesg|
|journalctl -k|systemdが管理するシステム起動時に出力されたメッセージを確認|dmesg|
|systemctl サブコマンド [ Unit名 ]|各サービスの稼働状況や起動設定を管理する|
|systemctl start|サービスを手動起動|
|systemctl stop|サービスを手動停止|
|systemctl set-default ターゲット名|次回起動時のターゲットを指定|
|systemctl restart|サービスを再起動|
|systemctl reload|サービスに設定ファイルを再読み込みさせる|
|systemctl reboot|システムを再起動させる|
|systemctl rescue|レスキューモード（ランレベル１）に入る|
|systemctl status|サービスの稼働状況|
|systemctl is-active|サービスが稼働しているかどうかを確認|
|systemctl enable|サービスの自動起動を有効にする|
|systemctl disable|サービスの自動起動を無効にする|
|systemctl default|デフォルトのモードにする|
|systemctl get-default ターゲット名|systemdで次回起動時のターゲットを確認||
|systemctl halt|システムを停止|
|systemctl poweroff|システムを停止|
|systemctl list-unit-files|すべてのUnitを表示|
|shutdown [オプション] 時間 [メッセージ]|時間（HH:MM）やM分後（+M）にshutdown||
|shutdown -h|シャットダウンする|
|shutdown -r|シャットダウン後にシステムを再起動する|
|shutdown -k|メッセージ通知のみを行う|
|shutdown -c|シャットダウンをキャンセルする|
|reboot|システムを再起動するが、時間およびメッセージを指定することはできない|
|init 6|ランレベルを6に変更しシステムを再起動||
|telinit 6|ランレベルを6に変更しシステムを再起動||
|shutdown -r now|システムを再起動||
|shutdown -k |シャットダウン処理を行わず、メッセージ通知のみを行う||
|systemctl reboot|システムを再起動||
|systemctl start reboot.target|システムを再起動||
|runlevel|現在および1つ前のランレベルを調べる||
|init ランレベル|ランレベルを変更||
|telinit ランレベル|ランレベルを変更||
|init Q/q|「/etc/inittab」を再読み込みさせ即座に変更を反映||
|telinit Q/q|「/etc/inittab」を再読み込みさせ即座に変更を反映||
|wall|ログイン中の全ユーザーにメッセージを送信<br>CentOS7 : wall [-n] [ message ]<br>Ubuntu 14.04 : wall [ file ]||

<br>
<br>

# ファイルシステム
|path|内容|確認方法|
|:---|:---|:---|
|/home|ユーザーごとのホームディレクトリ|-|
|/etc|システムやアプリケーションの設定情報|-|
|/etc/inittab|-|-|
|/etc/udev/rules.d|デバイスファイル作成時に使う設定ファイル（.rules）が配置。|-|
|/etc/modprobe.d/\*.conf|modprobeの設定ファイル（*.conf）が配置。|-|
|/etc/systemd/system/default.target|systemdでシステム起動時に最初に実行されるUnit|-|
|/lib/systemd/system|systemdのターゲットが格納|-|
|/bin|基本的なコマンドが配置 |-|
|/sbin|システム管理に必須のコマンドが配置|-|
|/proc|プロセス、ハードウェアおよびシステムリソースなどの情報を扱うための仮想的なファイルシステム|-|
|/proc/bus/pci/devices|PCIデバイス|cat/lspci|
|/proc/bus/usb/devices|接続されたUSBデバイスの情報|cat/lsusb|
|/proc/cmdline|ブートローダからカーネルに渡されたパラメータが確認できるファイル||
|/proc/cpuinfo|CPUに関する情報|cat/lscpu|
|/proc/dma|使用中のDMAチャネルに関する情報|-|
|/proc/interrups|IRQ(Interrupt ReQuest)（マウスやキーボードなどの周辺機器(デバイス)からCPUへの割り込み要求）|-|
|/proc/ioports|I/Oポートアドレス|-|
|/proc/memoinfo|メモリ|-|
|/proc/modules|ロードされているカーネルモジュール|-|
|/proc/scsi/scsi|SCSIデバイス|-|
|/sys|デバイスが接続されるとデバイス情報が作成される|-|
|/dev|ハードウェアのアクセスを抽象化したファイルであるデバイスファイルを格納。/sysの更新をudevが察知し、デバイスファイルが作成される。|-|
|/var/log/messages|Linuxでメインで使用されるログファイル|
|/var/log/secure|セキュリティに関するログ|
|/var/log/maillog|メールに関するログ|
|systemd-journald|systemdから起動したプロセスの標準出力やsyslogへのログメッセージをバイナリ形式で記録|-|

<br>
<br>

# 大容量記憶装置（ストレージ）
|名称|フラッシュメモリ<br>（不揮発性）|
|:---|:---|
|HDD（Hard Disk Drive）|-|
|USBフラッシュドライブ|○|
|SSD（Solid State Drive）|○|

<br>
<br>

# デバイスの種類

|名称|例|
|---|---|
|通信デバイス|NICカード、モデム|
|USBデバイス|USB|
|SCSI（スカジー）デバイス|-|

<br>
<br>

# USBデバイスクラス
|クラス名|サポートするデバイス|
|:---|:---|
|ACM Communication Device Class|モデム、TA(ターミナルアダプタ)|
|Audio Class|スピーカー、マイク|
|HID(Human Interface Device)|キーボード、マウス|
|Mass Storage Class|ハードディスク、USBメモリー|

<br>
<br>

# modprobeの設定ファイル

|名称|意味|
|:---|:---|
|options|各カーネルモジュールのデフォルトパラメータを指定|
|alias|カーネルモジュールに別名をつける|
|install|特定のカーネルモジュールのロード時に実行されるコマンドを指定|
|remove|特定のカーネルモジュールのアンロード時に実行されるコマンドを指定|
|blacklist|ロードしたくないカーネルモジュールを指定|

<br>
<br>

# udevシステム

- udev  
    ホットプラグデバイスの制御を行う。

|path|内容|
|:---|:---|
|/sys|デバイスが接続されるとデバイス情報が作成される|
|/dev|ハードウェアのアクセスを抽象化したファイルであるデバイスファイルを格納。/sysの更新をudevが察知し、デバイスファイルが作成される。|
|/etc/udev/rules.d|デバイスファイル作成時に使う設定ファイル（.rules）が配置。|

<br>
<br>

# Linuxの起動システム

|||SysVinit|Upstart|systemd|
|:---|:---|:---|:---|:---|
|起動プロセス|名称|initプロセス|-|systemdプロセス|
|^|起動方法|順次起動|並列起動|並列起動|
|^|最初に実行|/sbin/init/|-|/etc/systemd/system/default.target|
|^|設定ファイル|/etc/inittab<br>※デフォルトのランレベルや、ランレベルに応じた動作の設定|-|-|
|プロセス管理||PID|-|cgroups<br>（カーネルの機能）|
|起動プロセスの番号||1|-|-|
|管理単位|名称|-|job|Unit<br>※設定ファイル|
|^|種類|-|-|service　サービスを起動<br>device　デバイスを表す<br>mount　ファイルシステムをマウントする<br>swap　スワップ領域を有効にする<br>target　複数のUnitをグループ化する<br>timer　指定した日時や間隔で処理を実行する|
|サービスの管理コマンド||-|initctl|systemctl サブコマンド unit名|
|ログの管理|名称|-|-|systemd-journald|
|^|表示コマンド|-|-|journalctl<br>※cat不可|
|サービス|名称|ランレベル|-|ターゲット|
|^|種類|【Red Hat/CentOS】<br>0 停止<br>1,S,s シングルユーザー <br>2,3,5 マルチユーザー<br>4 未使用<br>6 再起動<br>【Ubuntu】<br>0 停止<br>1,S,s シングルユーザー<br>2~5 マルチユーザー<br>6 再起動<br>|-|0 poweroff.target / runlevel0.target<br>1 rescue.target / runlevel1.target<br>3 multi-user.target / runlevel3.target<br>5 graphical.target / runlevel5.target|
|^|場所|/etc/rc[0-6].d|-|/lib/systemd/system/[ターゲット名].target<br>※シンボリックリンク|
|^|確認|runrevel|-|-|
|^|変更|init <br>telinit|||


- /etc/init.d<br>各種サービスの起動に使うスクリプトが入っているディレクトリ
- /etc/rc[0-6].d/[ファイル名]の命名規則<br>
    - 1文字目：S（Start: サービスを起動）、K（Kill: サービスを停止）
    - 数字：実行優先順位。若番のものが先に実行される
    - サービス名：任意の名前をつける

# Linuxシステムが起動するまでの流れ

1. BIOS/UEFIが起動
2. BIOS/UEFIがハードウェアのチェック・初期化を行う
3. 起動デバイスに書き込まれたブートローダを読み出す
4. ブートローダに制御を移す
5. ブートローダが起動デバイス上からカーネルと初期RAMディスクをメモリ上へ読み込む
6. カーネルがメモリの初期化やシステムクロックの設定等を行う
7. カーネルが仮のルートファイルシステム（initramfs：初期RAMディスク）をマウントする
8. カーネルが最初のプロセスであるinit/systemdプロセスを実行する

# UEFI/BIOS

|||UEFI|BIOS|
|:---|:---|:---|:---|
|操作||GUI|CUI|
|ESP（最初にアクセスされる領域）||/boot/efi|-|
|パーティション|形式|GTP|-|
|^|上限|9.4ZB|2.2TB|


# 