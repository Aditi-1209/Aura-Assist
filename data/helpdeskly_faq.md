# HelpDeskly Help Center — Frequently Asked Questions

## Account & Billing

**Q: How do I reset my password?**
Go to the login page and click "Forgot password," then enter the email address associated with your HelpDeskly account. You'll receive a reset link valid for 60 minutes. If you don't see the email within a few minutes, check your spam folder before requesting a new link.

**Q: I forgot my password — what should I do?**
Use the "Forgot password" link on the sign-in screen to trigger a reset email. Click the link within 60 minutes and choose a new password that meets our minimum security requirements. For security reasons, the reset link can only be used once.

**Q: What pricing plans does HelpDeskly offer?**
HelpDeskly offers four plans: Starter, Growth, Scale, and Enterprise. Starter is designed for small teams with basic ticket queues and email support, while Growth adds SLA timers, macros, and reporting dashboards. Scale includes multi-channel support and advanced automation, and Enterprise adds custom contracts, dedicated onboarding, and SSO.

**Q: How do I upgrade or downgrade my subscription?**
Navigate to Settings > Billing > Plan Details and click "Change Plan." You can move between Starter, Growth, Scale, and Enterprise at any time, and the price difference is prorated automatically for the current billing cycle. Downgrades take effect at the start of your next billing cycle to avoid losing in-progress data.

**Q: Can I get an invoice for my HelpDeskly subscription?**
Yes, all invoices are automatically generated and available under Settings > Billing > Invoices. You can download them as PDFs or have them emailed to your billing contact each month. Enterprise customers can also request custom invoicing terms through their account manager.

**Q: What happens if my payment fails?**
We'll automatically retry the charge three times over seven days and notify your billing contact by email after each attempt. If payment still fails after the third retry, your account is moved to a restricted state where ticket queues become read-only until billing is resolved. You can update your payment method at any time during this window to restore full access immediately.

**Q: How do I cancel my HelpDeskly account?**
You can cancel anytime from Settings > Billing > Plan Details by selecting "Cancel Subscription." Your account remains active until the end of the current billing period, and you'll retain access to ticket queues and exported data until then. After cancellation, your data is retained for 30 days before permanent deletion.

**Q: Is there a free trial available?**
Yes, every new account starts with a 14-day free trial of the Growth plan, including full access to macros, SLA timers, and reporting. No credit card is required to start the trial. At the end of the trial you can choose to subscribe to any plan or continue on a limited free tier with reduced ticket queue capacity.

**Q: Do you offer discounts for nonprofits or annual billing?**
Yes, we offer a 20% discount for annual billing on the Growth, Scale, and Enterprise plans, applied automatically at checkout. Verified nonprofit organizations receive an additional 15% discount — contact our billing team through the in-app chat widget to apply. Discounts cannot currently be combined with custom Enterprise contract pricing.

**Q: How many agent seats are included in each plan?**
Starter includes up to 3 agent seats, Growth includes up to 10, and Scale includes up to 25, with additional seats available for purchase on all plans. Enterprise plans include custom seat counts negotiated with your account manager. Seat usage can be reviewed anytime under Settings > Billing > Usage.

## Setup & Installation

**Q: How do I install the HelpDeskly chat widget on my website?**
From Settings > Channels > Chat Widget, copy the provided JavaScript snippet and paste it before the closing `</body>` tag on your site. The widget will appear within a few minutes and automatically begins routing new conversations into your ticket queues. You can customize colors, position, and greeting text from the same settings page.

**Q: What's the process for setting up my email support channel?**
Go to Settings > Channels > Email and either connect your existing support address via forwarding or use the dedicated @yourcompany.helpdeskly.com address we provide. Incoming emails automatically create tickets in your default queue and replies sync back to the customer's inbox. DNS verification (SPF/DKIM) is recommended to improve deliverability.

**Q: How do I add new agents to my HelpDeskly account?**
Go to Settings > Team > Agents and click "Invite Agent," then enter their email address and assign a role. They'll receive an invitation link to set up their password and join your workspace. Seat limits depend on your plan, so confirm you have available seats under Settings > Billing > Usage before sending invites.

**Q: I'm trying to set up SSO but it's not working — what should I check?**
SSO is available on Scale and Enterprise plans under Settings > Security > Single Sign-On. Double-check that your Identity Provider's metadata URL and certificate are entered correctly, and that your domain has been verified. If login still fails, check that the email domain of the test user matches a verified domain in your SSO configuration.

**Q: How do I create my first ticket queue?**
Navigate to Settings > Queues > Add Queue and give it a name, such as "General Support" or "Billing Issues." You can then set routing rules to automatically assign incoming tickets from specific channels or keywords into that queue. Most teams start with two or three queues and expand as ticket volume grows.

**Q: Can I migrate my existing tickets from another helpdesk tool?**
Yes, HelpDeskly supports CSV import for ticket history under Settings > Data > Import, and we offer guided migration assistance for Scale and Enterprise customers. Make sure your export includes ticket status, timestamps, and customer email addresses for the cleanest import. Migrated tickets are placed in a queue called "Imported Tickets" by default, which you can rename or reorganize afterward.

**Q: How do I set up SLA timers for my team?**
Go to Settings > SLA Timers and define response and resolution targets for each priority level, such as Urgent, High, Normal, and Low. Timers start automatically when a ticket enters a queue and pause during business-hours-off periods if you've configured business hours. You'll see a live countdown on each ticket so agents know how much time remains.

**Q: What do I need to do to set up business hours?**
Under Settings > Business Hours, define your team's working days and hours per time zone, including any holiday exceptions. This affects how SLA timers calculate due dates and when auto-responses mention expected reply times. You can set different business hours for different queues if your teams operate across regions.

**Q: How do I install HelpDeskly's mobile app for my agents?**
The HelpDeskly mobile app is available on the iOS App Store and Google Play under the name "HelpDeskly Agent." Agents log in with their existing credentials, and push notifications for new tickets and SLA timer warnings are enabled by default. The mobile app supports ticket queues, macros, and internal notes, though some advanced reporting features are desktop-only.

**Q: Do I need to install anything to use HelpDeskly, or is it fully web-based?**
HelpDeskly runs entirely in your browser, so no software installation is required for agents or administrators. The only "installation" step is adding the chat widget snippet to your website if you want live chat support. We recommend the latest versions of Chrome, Firefox, Edge, or Safari for the best experience.

## Features & Usage

**Q: What are macros and how do I use them?**
Macros, also called canned responses, are pre-written replies you can insert into a ticket with one click to save time on common questions. Create them under Settings > Macros > Add Macro, where you can include dynamic fields like the customer's name or ticket ID. Agents can access macros directly from the reply editor using the lightning bolt icon.

**Q: What's the difference between a macro and a canned response?**
In HelpDeskly, "macro" and "canned response" refer to the same feature — a reusable reply template accessible from the ticket reply editor. We use both terms interchangeably throughout the product and documentation. You'll find them all managed in one place under Settings > Macros.

**Q: How do ticket queues work?**
Ticket queues are organized lists of incoming tickets, grouped by criteria like channel, priority, or team. Agents can be assigned to one or more queues, and tickets move between queues automatically based on routing rules you define in Settings > Queues. Each queue displays its own SLA timer status so agents can prioritize at a glance.

**Q: Can I set up automatic ticket routing?**
Yes, under Settings > Automation > Routing Rules, you can route tickets to specific queues or agents based on conditions like channel, keywords, customer tag, or priority. Rules are evaluated in order, so more specific rules should be placed above general ones. You can test routing rules against sample tickets before activating them.

**Q: How do I view reports on my team's ticket performance?**
The Reports tab provides dashboards on metrics like average response time, SLA compliance, ticket volume by queue, and agent performance, available on Growth plans and above. You can filter by date range, queue, or individual agent, and export any report as a CSV. Scale and Enterprise plans also include customizable report builders.

**Q: What's the best way to add internal notes to a ticket?**
Click "Add Internal Note" within any ticket to leave comments visible only to your team, not the customer. Internal notes support @mentions to notify specific agents and can include file attachments. They're commonly used to flag escalations or share context before handing off a ticket.

**Q: How do customer satisfaction (CSAT) surveys work?**
CSAT surveys can be enabled under Settings > Surveys and are automatically sent after a ticket is marked resolved, asking customers to rate their experience. Results appear on the ticket itself and roll up into the Reports dashboard for trend analysis. You can customize the survey question and rating scale to match your brand voice.

**Q: Can I tag tickets for better organization?**
Yes, you can apply tags to tickets manually or automatically via routing rules, and use them to filter views, trigger automations, or build reports. Common tags include things like "billing," "bug," or "feature-request." Tags are managed centrally under Settings > Tags to avoid duplicates across your team.

**Q: How do I merge duplicate tickets?**
Open one of the duplicate tickets, click the "Merge" option in the ticket actions menu, and search for the other ticket by ID or customer email. Merging combines the conversation history into a single ticket and closes the duplicate automatically. The customer only receives replies from the primary ticket going forward.

**Q: What's the difference between Starter and Growth plan features?**
Starter includes core ticket queues, email support, and basic macros, suitable for small teams handling lower ticket volume. Growth adds SLA timers, CSAT surveys, advanced reporting, and a higher macro limit. Scale and Enterprise build further on Growth with multi-channel routing, custom report builders, and SSO.

## Troubleshooting

**Q: The chat widget isn't appearing on my website — what should I check?**
First, confirm the JavaScript snippet from Settings > Channels > Chat Widget is placed before the closing `</body>` tag and hasn't been altered. Clear your browser cache and check the browser console for any script-blocking errors from ad blockers or content security policies. If the widget still doesn't load, verify the widget is toggled "Active" in your channel settings.

**Q: Why isn't the live chat widget showing up on my site?**
This is usually caused by an incorrect snippet placement, a content security policy blocking external scripts, or the widget being set to inactive. Check Settings > Channels > Chat Widget to confirm it's enabled, and inspect your browser's developer console for blocked requests. If you recently changed your site's CSP headers, you may need to allowlist `*.helpdeskly.com`.

**Q: I'm not receiving email notifications for new tickets — how do I fix this?**
Check Settings > Notifications to confirm your notification preferences are enabled for new ticket alerts. Also check your email provider's spam or quarantine folder, since automated notification emails are sometimes filtered. If the issue persists, ask your IT team to allowlist our sending domain, helpdeskly-notify.com.

**Q: SLA timers aren't pausing during my configured business hours — why?**
This typically happens when a queue isn't linked to the correct business hours profile under Settings > Business Hours. Open the queue settings and confirm the right business hours profile is selected, since each queue can use a different one. If you recently changed time zones, double-check the profile reflects the updated zone before re-saving.

**Q: My imported tickets are missing timestamps — what happened?**
This usually means the CSV file used for import didn't include a properly formatted timestamp column, or the format didn't match our expected ISO 8601 standard. Re-export your data with timestamps in the format YYYY-MM-DDTHH:MM:SS and re-run the import under Settings > Data > Import. Contact support if the issue continues after a corrected re-import.

**Q: Why can't I log into my HelpDeskly account?**
First, confirm you're using the correct email address and that Caps Lock isn't affecting your password entry. If you've enabled SSO, make sure you're using the "Sign in with SSO" option rather than the standard password field. If you're still locked out, use the "Forgot password" link or contact your workspace administrator to check your account status.

**Q: Tickets are routing to the wrong queue — how do I fix this?**
Review your routing rules under Settings > Automation > Routing Rules, since rules are evaluated top-to-bottom and an earlier broad rule may be catching tickets meant for a more specific one. Reorder rules so specific conditions sit above general fallback rules. You can use the rule tester to simulate a sample ticket and confirm it lands in the expected queue.

**Q: Why are my reports showing no data for a selected date range?**
This usually happens when the selected date range falls outside your plan's report retention window, or filters like queue or agent are too narrow. Starter plans retain 30 days of report history, while Growth and above retain 12 months. Try widening the date range or removing filters one at a time to identify the cause.

**Q: The mobile app isn't sending push notifications — what can I do?**
Confirm notifications are enabled both in your device's system settings and within the HelpDeskly Agent app under Settings > Notifications. Make sure you're logged into the same workspace and agent account you use on desktop. Reinstalling the app or toggling notification permissions off and back on often resolves delivery issues.

**Q: I accidentally merged the wrong tickets — can this be undone?**
Yes, contact support within 24 hours of the merge through the in-app chat widget, and our team can manually split the tickets back apart. After 24 hours, merged conversation history becomes harder to separate cleanly, though we can still attempt it on a best-effort basis. To avoid this, always confirm the ticket ID and customer email before confirming a merge.

## Integrations

**Q: Does HelpDeskly integrate with Slack?**
Yes, the Slack integration can be enabled under Settings > Integrations > Slack, and it posts real-time notifications for new tickets, SLA timer warnings, and @mentions into channels you choose. Agents can also reply to tickets directly from Slack using slash commands. This integration is available on Growth plans and above.

**Q: Can I connect HelpDeskly to my Slack workspace for notifications?**
Yes, go to Settings > Integrations > Slack and authorize the connection with your Slack workspace. You can choose which events trigger notifications, such as new tickets, SLA breaches, or customer replies, and route them to specific channels. This feature requires a Growth plan or higher.

**Q: How do I connect HelpDeskly with Zendesk-style ticketing channels?**
HelpDeskly supports importing and syncing channel data from Zendesk-style helpdesk systems via Settings > Integrations > Channel Sync, using an API key from your existing provider. Synced tickets appear in a dedicated queue and retain their original timestamps and customer history. This is commonly used during migration periods when running two systems in parallel.

**Q: What CRM integrations does HelpDeskly support?**
HelpDeskly integrates with major CRMs including Salesforce and HubSpot under Settings > Integrations > CRM, allowing customer ticket history to appear directly in CRM contact records. You can also trigger CRM workflows based on ticket tags or priority. This integration is available on Scale and Enterprise plans.

**Q: How do I set up a Zapier integration with HelpDeskly?**
Search for "HelpDeskly" in the Zapier app directory and connect it using an API key generated under Settings > Integrations > API Keys. From there, you can build Zaps that trigger on events like new tickets, resolved tickets, or CSAT responses. Zapier integration is available on all plans except Starter.

**Q: Can HelpDeskly integrate with my own custom application?**
Yes, our REST API, documented under Settings > Integrations > API Keys, allows you to create tickets, update statuses, and retrieve queue data programmatically. API access requires a Growth plan or higher, and rate limits scale with your plan tier. We also provide webhooks for real-time event notifications to your own systems.

**Q: Does HelpDeskly support webhooks?**
Yes, webhooks can be configured under Settings > Integrations > Webhooks to notify external systems when events occur, such as ticket creation, status changes, or SLA breaches. Each webhook can be scoped to specific queues or tags to reduce noise. Failed webhook deliveries are retried automatically up to five times.

**Q: How do I integrate HelpDeskly with Microsoft Teams?**
Enable the Teams integration under Settings > Integrations > Microsoft Teams and authorize access to your organization's workspace. Once connected, you'll receive ticket notifications and can reply to customers directly from a Teams channel, similar to our Slack integration. This integration is available on Growth plans and above.

**Q: Can I sync HelpDeskly tickets with a project management tool like Jira?**
Yes, the Jira integration under Settings > Integrations > Jira lets you convert tickets into Jira issues with a single click, useful for escalating bugs to engineering teams. Updates to the linked Jira issue can optionally sync back as internal notes on the original ticket. This integration is available on Scale and Enterprise plans.

**Q: Where do I find or generate an API key for HelpDeskly?**
Go to Settings > Integrations > API Keys and click "Generate New Key," giving it a descriptive label so you can track its usage. Keys are tied to your workspace and inherit permissions based on the role of the agent who created them. You can revoke a key at any time if it's no longer needed or may have been compromised.

## Security & Privacy

**Q: How does HelpDeskly protect my customers' data?**
All data is encrypted in transit using TLS 1.2 or higher and encrypted at rest using AES-256. We perform regular third-party security audits and maintain SOC 2 Type II compliance. Access to production systems is restricted to authorized personnel and logged for auditing purposes.

**Q: Is HelpDeskly SOC 2 compliant?**
Yes, HelpDeskly maintains SOC 2 Type II certification, and our most recent audit report is available to Scale and Enterprise customers upon request through your account manager. We undergo annual re-certification to ensure continued compliance. Summary documentation is also available on our trust center page.

**Q: Does HelpDeskly support single sign-on (SSO)?**
Yes, SSO via SAML 2.0 is available on Scale and Enterprise plans under Settings > Security > Single Sign-On. We support major identity providers including Okta, Azure AD, and Google Workspace. Enabling SSO does not remove the ability for administrators to use password-based emergency access.

**Q: Can I enforce two-factor authentication (2FA) for my team?**
Yes, under Settings > Security > Authentication, administrators can require all agents to enable 2FA before accessing the workspace. We support authenticator apps via TOTP as well as SMS-based codes. Enforcing 2FA is available on all plans, including Starter.

**Q: How long does HelpDeskly retain my data after I cancel?**
After cancellation, your account data, including tickets and customer records, is retained for 30 days in case you choose to reactivate. After that period, data is permanently deleted from production systems and purged from backups within an additional 30 days. You can request earlier deletion by contacting support through the chat widget.

**Q: Where is HelpDeskly's data hosted?**
HelpDeskly hosts customer data in SOC 2-audited data centers located in the United States, with an optional European data residency add-on for Scale and Enterprise customers. Data residency settings are configured during onboarding and cannot be changed without a data migration request. Backups are encrypted and stored redundantly across multiple availability zones.

**Q: Does HelpDeskly comply with GDPR?**
Yes, HelpDeskly is fully GDPR compliant and offers a Data Processing Addendum (DPA) that can be signed digitally under Settings > Legal > Agreements. We support data subject access requests, the right to erasure, and data portability requests submitted through our privacy contact. EU customers can also opt into our European data residency add-on for additional compliance assurance.

**Q: Who can access my company's ticket data within HelpDeskly?**
Access is limited to agents and administrators within your workspace based on role-based permissions configured under Settings > Team > Roles. HelpDeskly support staff only access your data with explicit permission, typically during a support request, and all such access is logged. You can review an access log for your workspace under Settings > Security > Audit Log.

**Q: Can I restrict which IP addresses are allowed to log into our workspace?**
Yes, IP allowlisting is available on Enterprise plans under Settings > Security > IP Restrictions, allowing administrators to limit login access to specified IP ranges. Attempts from outside the allowed ranges are blocked and logged in the audit log. This is commonly used by organizations requiring office-network-only access to sensitive ticket data.

**Q: What should I do if I suspect unauthorized access to my account?**
Immediately change your password and revoke any active sessions under Settings > Security > Active Sessions. Enable 2FA if it isn't already active, and review the audit log under Settings > Security > Audit Log for unfamiliar activity. Contact our security team through the in-app chat widget so we can investigate and assist with securing your account.
