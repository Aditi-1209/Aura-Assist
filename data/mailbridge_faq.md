# MailBridge Help Center — Frequently Asked Questions

## Account & Billing

**Q: What pricing plans does MailBridge offer?**
MailBridge offers four plans based on subscriber count: Starter (up to 1,000 subscribers), Growth (up to 10,000 subscribers), Pro (up to 50,000 subscribers), and Enterprise (50,000+ subscribers with custom pricing). Each plan includes access to the Campaign Builder and Template Library, with higher tiers unlocking Automation Workflows, Audience Segments, and A/B Testing. You can compare plan details anytime from the Billing tab in your account settings.

**Q: How do I upgrade or downgrade my subscription?**
Go to Account Settings > Billing > Change Plan, select the new tier, and confirm the change. Upgrades take effect immediately and are prorated for the current billing cycle, while downgrades apply at the start of your next billing cycle. If your subscriber count exceeds your new plan's limit, MailBridge will prompt you to reduce your audience before the downgrade is finalized.

**Q: I forgot my password. What should I do?**
Click "Forgot password?" on the login page and enter the email address associated with your MailBridge account. You'll receive a password reset link valid for 30 minutes. If the email doesn't arrive within a few minutes, check your spam folder or contact support@mailbridge.io for assistance.

**Q: How do I reset my password?**
Navigate to the login screen and select "Forgot password?", then follow the emailed instructions to set a new password. For security, the reset link expires after 30 minutes, so request a new one if it lapses. Once reset, you'll be logged out of all active sessions and need to sign in again.

**Q: Can I add team members to my account?**
Yes, all plans except Starter support multiple team members with role-based permissions such as Admin, Editor, and Viewer. To invite someone, go to Account Settings > Team and enter their email address. Pro and Enterprise plans support unlimited team seats, while Growth is limited to five.

**Q: What happens to my data if I cancel my subscription?**
Your campaigns, audience segments, and analytics history remain accessible in read-only mode for 30 days after cancellation. After that period, your data is permanently deleted from MailBridge servers in accordance with our retention policy. You can export your subscriber lists and campaign reports at any time before the 30-day window closes.

**Q: How do I update my billing information?**
Go to Account Settings > Billing > Payment Method and enter your new card details or billing address. Changes take effect immediately and apply to your next invoice. MailBridge accepts all major credit cards as well as ACH payments for Pro and Enterprise customers.

**Q: Why was my payment declined?**
Payments are typically declined due to expired cards, insufficient funds, or a billing address mismatch with your bank. Check your payment method under Account Settings > Billing and update it if needed. MailBridge automatically retries failed payments three times over five days before pausing your account.

**Q: Does MailBridge offer a free trial?**
Yes, new accounts receive a 14-day free trial of the Growth plan, which includes Automation Workflows and A/B Testing. No credit card is required to start the trial. At the end of the trial, you can choose a paid plan or your account will automatically move to a limited free tier.

**Q: How do I close my MailBridge account permanently?**
Go to Account Settings > Billing > Cancel Subscription, then select "Delete Account Permanently" on the confirmation screen. This immediately stops billing and schedules your data for deletion after the standard 30-day retention window. If you only want to pause sending, consider downgrading instead of deleting your account.

## Setup & Installation

**Q: How do I create my first MailBridge account?**
Visit mailbridge.io/signup and enter your email address, company name, and a password to get started. You'll be guided through a short onboarding flow that helps you import contacts and create your first campaign. No credit card is required until you choose to upgrade beyond the free trial.

**Q: How do I import my existing subscriber list?**
From the dashboard, go to Audience > Import and upload a CSV file or connect a supported integration like Shopify or WordPress to sync contacts automatically. MailBridge will map your CSV columns to fields such as email, first name, and tags during the import wizard. Large lists over 10,000 contacts may take a few minutes to process.

**Q: What do I need to do to verify my sending domain?**
Go to Settings > Domains > Add Domain and enter your domain name, then add the provided SPF, DKIM, and DMARC records to your DNS provider. Domain verification typically completes within a few hours but can take up to 48 hours depending on DNS propagation. Verifying your domain improves deliverability and removes the "via MailBridge" tag from your emails.

**Q: How long does domain verification take?**
Most domains verify within a few hours of adding the required DNS records, though propagation can occasionally take up to 48 hours. You can check verification status anytime under Settings > Domains. If verification stalls past 48 hours, double-check that the DKIM and SPF records were entered exactly as provided.

**Q: How do I set up my company profile and sender details?**
Go to Settings > Sender Profile and fill in your company name, physical mailing address, and default reply-to email. This information appears in the footer of every campaign to comply with anti-spam regulations like CAN-SPAM and GDPR. You can create multiple sender profiles if you manage several brands from one account.

**Q: Can I migrate from another email marketing tool to MailBridge?**
Yes, MailBridge supports CSV import for contacts and offers guided migration assistance for accounts moving from major competitors. Our support team can help map existing automation workflows and audience segments during onboarding on Pro and Enterprise plans. Reach out to support@mailbridge.io to request a migration consultation.

**Q: How do I install the MailBridge tracking snippet on my website?**
Go to Settings > Tracking Code, copy the JavaScript snippet, and paste it before the closing `</head>` tag on your website. This snippet enables website activity tracking, which feeds into Audience Segments and Automation Workflows. If you use WordPress or Shopify, the official MailBridge plugin installs this automatically.

**Q: What's the easiest way to connect MailBridge with my WordPress site?**
Install the MailBridge for WordPress plugin from the WordPress plugin directory, then enter your API key from Settings > API Keys to connect your account. The plugin automatically syncs new commenters and customers into your chosen Audience Segment. You can also embed signup forms built in the Campaign Builder directly into WordPress pages or widgets.

**Q: How do I set up a signup form for my website?**
Go to Audience > Forms > Create Form, choose a template, and customize the fields and design using the drag-and-drop editor. Once published, copy the embed code or use the direct link to add the form to your site. Form submissions automatically create or update contacts in the Audience Segment you select.

**Q: Do I need any technical skills to get started with MailBridge?**
No coding experience is required to use the Campaign Builder, Template Library, or signup forms, since everything uses a drag-and-drop interface. Basic DNS knowledge is helpful for domain verification, but our setup guides walk you through each step. Developers can go further using the MailBridge API and Zapier integration for custom workflows.

## Features & Usage

**Q: What is the Campaign Builder and how do I use it?**
The Campaign Builder is MailBridge's drag-and-drop editor for designing email campaigns using pre-built blocks for text, images, buttons, and product showcases. Choose a starting point from the Template Library or build from a blank canvas, then preview how your email renders across devices before sending. Campaigns can be sent immediately, scheduled for later, or triggered through an Automation Workflow.

**Q: How do Automation Workflows work?**
Automation Workflows let you build multi-step email sequences triggered by events such as a new signup, an abandoned cart, or a tag added to a contact. Each workflow uses a visual flowchart where you add delays, conditions, and branching paths based on subscriber behavior. Workflows run continuously in the background once activated, without requiring manual sends.

**Q: What are Audience Segments and how do I create one?**
Audience Segments are saved groups of contacts filtered by criteria like engagement history, purchase behavior, tags, or custom fields. Go to Audience > Segments > Create Segment, set your filter conditions, and save it for use in campaigns and Automation Workflows. Segments update dynamically as contacts meet or no longer meet the defined criteria.

**Q: How does A/B Testing work in MailBridge?**
A/B Testing lets you create two or more variations of a campaign — testing subject lines, content, or send times — and automatically sends the winning version to the rest of your audience. Set your test size, winning metric (open rate or click rate), and test duration when configuring the campaign in the Campaign Builder. Results are available in the Analytics Dashboard once the test concludes.

**Q: Can I schedule campaigns to send at a specific time?**
Yes, in the Campaign Builder's final review step, choose "Schedule for Later" and select your desired date and time. MailBridge also offers Send Time Optimization, which automatically delivers each contact's email when they're historically most likely to open it. Scheduled campaigns can be edited or canceled anytime before the send time.

**Q: What kind of reporting does the Analytics Dashboard provide?**
The Analytics Dashboard shows open rates, click-through rates, bounce rates, unsubscribes, and revenue attribution for ecommerce integrations like Shopify. You can view performance by individual campaign, by Automation Workflow, or aggregated across a custom date range. Reports can be exported as CSV or scheduled for automatic email delivery to your team.

**Q: How do I use the Template Library?**
Go to Campaigns > New Campaign > Browse Templates to choose from categories like newsletters, promotions, and product announcements. Templates are fully customizable in the Campaign Builder, and you can save your own designs back to the library for reuse. Pro and Enterprise plans include access to premium template collections updated monthly.

**Q: Is there a way to personalize emails with subscriber data?**
Yes, the Campaign Builder supports merge tags that pull in subscriber data such as first name, location, or custom fields collected through signup forms. You can also use conditional content blocks that show different content to different Audience Segments within the same campaign. Personalization is also supported inside Automation Workflows for dynamic, behavior-based messaging.

**Q: How do I duplicate a campaign I've already sent?**
Open the campaign from your Campaigns list, click the three-dot menu, and select "Duplicate." This creates an editable copy in the Campaign Builder with all design elements intact, while resetting the send status so you can schedule it again. Duplicating is useful for recurring newsletters or seasonal promotions.

**Q: Can I preview how my email looks on mobile devices?**
Yes, the Campaign Builder includes a live preview toggle that switches between desktop and mobile views as you design. You can also send a test email to yourself or your team to check rendering across real email clients. We recommend testing on at least two device types before scheduling a send to your full Audience Segment.

## Troubleshooting

**Q: My campaign emails are going to spam. How do I fix this?**
First, verify your sending domain under Settings > Domains to ensure SPF, DKIM, and DMARC records are correctly configured, as unverified domains are far more likely to be filtered. Review your content for spam-trigger words and excessive links, and check your sender reputation in the Analytics Dashboard. Maintaining a clean Audience Segment by removing inactive or bounced contacts also significantly improves deliverability.

**Q: Why is my open rate suddenly so low?**
A sudden drop usually points to deliverability issues, an unverified sending domain, or major email clients like Apple Mail and Gmail applying stricter privacy protections that affect open tracking. Check the Analytics Dashboard for a spike in bounces or spam complaints around the same time. If the issue persists, contact support@mailbridge.io with the affected campaign ID for a deeper deliverability review.

**Q: I can't log into my MailBridge account. What should I check?**
Confirm you're using the correct email address and that Caps Lock isn't affecting your password entry. If you've forgotten your password, use the "Forgot password?" link on the login page to reset it. If your account was suspended for a billing issue, you'll see a notice on the login screen with instructions to resolve it.

**Q: My Automation Workflow isn't triggering for new contacts.**
Check that the workflow's trigger condition matches how the contact entered your account, such as a specific signup form or Audience Segment. Confirm the workflow status shows "Active" rather than "Draft" or "Paused" in the Automation Workflows dashboard. Also verify the contact doesn't already meet a workflow's "exit" condition, which would prevent re-entry.

**Q: Why did my campaign fail to send?**
Failed sends are usually caused by an unverified sending domain, exceeding your plan's monthly send limit, or a paused account due to a billing issue. Check the campaign status page for a specific error message, which will indicate the exact cause. If the issue isn't listed there, contact support with your campaign ID for further investigation.

**Q: Some of my images aren't displaying in sent emails.**
This is often caused by broken image links, files exceeding the 5MB size limit, or email clients blocking images by default until the recipient clicks "Display images." Re-upload affected images through the Campaign Builder's media library to ensure they're hosted on MailBridge's CDN. Adding descriptive alt text also helps maintain context when images are blocked.

**Q: My CSV import keeps failing. What's wrong?**
Check that your CSV file is UTF-8 encoded and that the email column doesn't contain blank or malformed addresses. Files larger than 50MB should be split into smaller batches before importing. If specific rows fail, MailBridge generates an error report after the import attempt that lists the exact rows and reasons for rejection.

**Q: Why do I see a high bounce rate on my last campaign?**
High bounce rates typically indicate an outdated subscriber list with many invalid or inactive addresses. Run your Audience Segment through list cleaning before your next send, and remove contacts that have hard-bounced previously, since MailBridge automatically suppresses them going forward. Bounce rates above 5% can also temporarily affect your sender reputation across future campaigns.

**Q: The A/B Testing results don't seem to be showing for my campaign.**
A/B Testing results typically need the full test duration to elapse before the winning variant is determined and reported in the Analytics Dashboard. If your audience segment is too small, MailBridge may not gather statistically significant data within the configured window. Double-check the test was set up with a clear winning metric, such as open rate or click rate, before the campaign was sent.

**Q: My Zapier integration stopped working. How do I troubleshoot it?**
Check the Zapier dashboard for any error notifications on the affected Zap, as expired authentication tokens are the most common cause. Reconnect your MailBridge account in Zapier under the app connection settings to refresh the API credentials. If the Zap still fails, verify that the trigger event, such as new subscriber, still matches an active Audience Segment in MailBridge.

## Integrations

**Q: What integrations does MailBridge support?**
MailBridge integrates natively with Shopify, WordPress, Zapier, Salesforce, and Google Analytics, with more integrations added regularly. These connections allow automatic contact syncing, ecommerce revenue tracking, and triggering Automation Workflows from external events. A full list of available integrations is in Settings > Integrations.

**Q: How do I connect my Shopify store to MailBridge?**
Go to Settings > Integrations > Shopify and click "Connect," then authorize MailBridge through your Shopify admin panel. Once connected, customer data syncs automatically into your chosen Audience Segment, and order data becomes available for revenue reporting in the Analytics Dashboard. You can also trigger Automation Workflows based on Shopify events like abandoned carts or completed purchases.

**Q: How does the WordPress integration work?**
Install the MailBridge for WordPress plugin, then enter your API key from Settings > API Keys to link your site. The plugin lets you embed signup forms built in the Campaign Builder and automatically adds new WordPress users or commenters to a specified Audience Segment. Updates to contact data sync in near real time.

**Q: Can I use Zapier with MailBridge?**
Yes, MailBridge has an official Zapier integration that connects to thousands of other apps using triggers like "new subscriber" or "campaign sent" and actions like "add contact to segment." Go to Zapier, search for MailBridge, and authenticate using your API key from Settings > API Keys. This is the recommended option for connecting tools that don't have a native MailBridge integration.

**Q: Does MailBridge integrate with Salesforce?**
Yes, the Salesforce integration syncs contacts and leads bidirectionally between MailBridge and your Salesforce CRM, available on Pro and Enterprise plans. You can map MailBridge Audience Segments to Salesforce campaigns and trigger Automation Workflows based on changes to Salesforce lead status. Setup is available under Settings > Integrations > Salesforce.

**Q: How do I track website conversions with Google Analytics?**
Connect your Google Analytics account under Settings > Integrations > Google Analytics, and MailBridge will automatically append UTM parameters to links in your campaigns. This allows you to track email-driven traffic and conversions directly within your Google Analytics reports. Combined with the Analytics Dashboard, you get a complete picture of campaign performance across both platforms.

**Q: Can I connect MailBridge to apps without a native integration?**
Yes, use the Zapier integration to connect MailBridge with thousands of supported apps, or use the MailBridge API directly for custom development. The API supports managing contacts, Audience Segments, and campaign sends programmatically. Full API documentation is available at developers.mailbridge.io.

**Q: Where do I find my API key?**
Go to Settings > API Keys and click "Generate New Key" if you don't already have one. Keep your API key confidential, since it grants programmatic access to your contacts and campaigns. You can revoke and regenerate a key anytime if you suspect it has been compromised.

**Q: Does MailBridge support webhooks?**
Yes, webhooks can be configured under Settings > Integrations > Webhooks to notify external systems of events like new subscribers, unsubscribes, or completed Automation Workflows. This is useful for syncing data with custom-built applications that aren't covered by our native integrations. Webhook payloads are delivered in JSON format with retry logic for failed deliveries.

**Q: Can I sync customer purchase history from Shopify into Audience Segments?**
Yes, once Shopify is connected, purchase data such as total spend, last order date, and purchased products becomes available as filter criteria when building an Audience Segment. This lets you target campaigns based on real purchase behavior, such as customers who haven't ordered in 60 days. Revenue from these segments also appears in the Analytics Dashboard's ecommerce reporting.

## Security & Privacy

**Q: How does MailBridge protect my account from unauthorized access?**
MailBridge supports two-factor authentication (2FA), which you can enable under Account Settings > Security. We also monitor for unusual login activity and notify account owners by email of sign-ins from new devices or locations. Passwords are stored using industry-standard hashing and are never visible to MailBridge staff.

**Q: Is my subscriber data encrypted?**
Yes, all data is encrypted in transit using TLS 1.2 or higher and encrypted at rest using AES-256 encryption. This applies to contact information, campaign content, and analytics data stored on MailBridge servers. Our infrastructure undergoes regular third-party security audits to verify these protections remain effective.

**Q: Is MailBridge GDPR compliant?**
Yes, MailBridge provides tools to support GDPR compliance, including consent tracking on signup forms, data export requests, and the ability to permanently delete contact records on request. We act as a data processor under GDPR, and our Data Processing Addendum is available in Settings > Legal. Customers remain responsible for obtaining proper consent before adding contacts to their Audience Segments.

**Q: How do I enable two-factor authentication?**
Go to Account Settings > Security > Two-Factor Authentication and follow the prompts to link an authenticator app like Google Authenticator or Authy. Once enabled, you'll need a time-based code in addition to your password to log in. We recommend enabling 2FA for all team members with Admin-level access.

**Q: Who at MailBridge can see my contact data?**
Access to customer data is restricted to authorized MailBridge employees who need it to provide support, and all access is logged for audit purposes. We never sell or share your subscriber data with third parties for marketing purposes. You can review our full data handling practices in our Privacy Policy, linked in the account footer.

**Q: What happens to subscriber data if a contact unsubscribes?**
Unsubscribed contacts are immediately suppressed from all future campaigns and Automation Workflows while remaining in your account for compliance and audit purposes. You can still view their historical engagement data in the Analytics Dashboard, but you cannot re-add them to active sending without explicit reconfirmation. This suppression list is honored automatically across all Audience Segments.

**Q: Does MailBridge comply with CAN-SPAM requirements?**
Yes, MailBridge requires every campaign to include a physical mailing address and a functional unsubscribe link, both enforced automatically by the Campaign Builder before a send is allowed. Unsubscribe requests are processed immediately and contacts are added to your suppression list. These safeguards are built in by default and cannot be disabled.

**Q: Can I request a copy of all data MailBridge has about my account?**
Yes, go to Account Settings > Privacy > Export My Data to request a full export of your account data, including campaigns, contacts, and analytics history. Exports are typically delivered within 48 hours as a downloadable archive. This feature supports both general data portability needs and formal GDPR data access requests.

**Q: How do I permanently delete a contact's data on request?**
Go to Audience > Contacts, search for the contact, and select "Delete Permanently" from their profile menu to remove all personal data associated with them. This action is irreversible and removes the contact from all Audience Segments, campaign history, and Automation Workflows. Permanent deletion requests are typically used to fulfill GDPR right-to-erasure obligations.

**Q: Where are MailBridge's servers located and is data stored securely?**
MailBridge's primary infrastructure is hosted in SOC 2 Type II certified data centers with redundant backups across multiple geographic regions. All data at rest is encrypted with AES-256, and access to physical infrastructure is tightly restricted and monitored. Customers on Enterprise plans can request data residency information specific to their compliance needs.
