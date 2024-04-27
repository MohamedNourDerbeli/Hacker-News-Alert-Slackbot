## 🤔 What is it?

This is a basic Slack Bot that:
1. Fetches top Hacker News stories
2. Filters them based on keywords
3. Sends a slack message to a list of users, notifying them of any matches.

Set-up and deployment takes only 5 minutes! With _Scheduled Deployments_, you can execute the script as often as you'd like.

![](assets/example.png)

## ⚡ Quick Configuration (Recommended) 

Want to get started as fast as possible? 

1. Head to [this page](https://api.slack.com/apps) and click `Create New App`
2. Select `From an app manifest`
3. Copy + paste the [manifest file](manifest.json)
4. Select "Install to Workspace"
5. Add in your Slack secrets (found below) to the secrets pane in Repit
6. Add your Slack UID (_Profile_ -> three dot menu -> _Copy member ID_) and keywords to the [app](https://replit.com/@replit-matt/Hackernews-Alert-Slackbot#app.py:68).
7. Run your Repl (select `Run` at the top of this page) + see what happens!

### 🔑 Secrets

| Secret                 | Description                                                                                                                                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SLACK_SIGNING_SECRET` | Your app's "signing secret" can be found on the main app page under Basic Information -> App Credentials -> Signing Secret.                                                          |
| `SLACK_APP_TOKEN`      | The [app-level token](https://api.slack.com/authentication/token-types#app) you configured when setting up Socket mode or under Basic Information -> App-Level Tokens -> Token Name. |
| `SLACK_BOT_TOKEN`      | Your app's bot token is in the Installed App Settings tab -> Bot User OAuth Token.                                                                                                   |

Add these to your Repl in the _Secrets_ pane (⌘ + K and type "secrets").

### 🎽 Deploying Your App

Once you have your application configured and tokens set, you can hit `Run` (⌘ + Enter) in Replit to execute `app.py`. 

To have your bot execute on a schedule, head over to "Deployments" (⌘ + K, "deployments") to create a "Scheduled" deployment. This deployment uses `cron` syntax to execute the job on a regular cadence.