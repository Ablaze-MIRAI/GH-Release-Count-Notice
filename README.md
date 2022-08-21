# GH-Release-Count-Notice

最新リリースのアセットダウンロード数をDiscord Webhookで通知します

## Use

Forkして`.github/workflow/send.yml`を任意の時刻に変更し、Settingsで環境変数を [#Dev](#dev) のように設定します。

##  Dev

1. リポジトリをクローン

2. 環境変数を設定します

```shell
# PowerShell
$env:DISCORD_WEBHOOK_URL = "https://discord.com/*****"
$env:TARGET_REPO_NAME = "Floorp-Projects/Floorp"
```