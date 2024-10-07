BASE_PROMPT = """
You are a world class video editor who also is a customer success manager. While reviewing a customer success call transcript, you are looking to analyze and find pain points of the customer and predict if they are going to churn. 
based on the full video transcript you were given, extract clips which the customer's positive or negative interaction with the product in a customer success call. Each clip that you find should be related to pain points like problems they have had with the product or any good points they have had with the product.
Each clip should be self explaining and convey core concepts as part of the analysis

Formatting Instructions
{format_instructions}

Transcript
{transcript}
"""

TRANSCRIPT = """
1
00:00:00,000 --> 00:00:03,500
[Customer Success Manager] Hi John, thanks for hopping on the call today! How are you doing?

2
00:00:03,500 --> 00:00:07,000
[Client] Hey, I'm doing well, thanks! Just eager to get some insights on the dashboard setup.

3
00:00:07,500 --> 00:00:11,200
[Customer Success Manager] Awesome! Let’s dive in. I understand you’re using our platform primarily for revenue operations, correct?

4
00:00:11,300 --> 00:00:15,500
[Client] Yep, we have multiple data integrations flowing in, but I’m not sure if the dashboard is reflecting all the key metrics.

5
00:00:16,000 --> 00:00:19,800
[Customer Success Manager] Got it. Which integrations are you currently using?

6
00:00:20,000 --> 00:00:24,500
[Client] We're pulling data from Salesforce, HubSpot, and Stripe, but the dashboard feels a bit off in terms of what we expect to see.

7
00:00:25,000 --> 00:00:28,900
[Customer Success Manager] Okay, I see. Can you describe the discrepancies you’re noticing?

8
00:00:29,200 --> 00:00:34,200
[Client] Yeah, so our MRR (Monthly Recurring Revenue) from Stripe isn’t matching what we have in our internal reports.

9
00:00:34,800 --> 00:00:39,000
[Customer Success Manager] Hmm, let me check if there's any misalignment in the data aggregation settings. 

10
00:00:39,100 --> 00:00:42,600
[Customer Success Manager] It could be that the Stripe data is being filtered incorrectly in the dashboard. 

11
00:00:43,000 --> 00:00:48,500
[Client] That would make sense, because the other integrations seem fine, but Stripe’s the one throwing us off.

12
00:00:49,000 --> 00:00:52,500
[Customer Success Manager] I’ll take a closer look at the configuration for that. 

13
00:00:53,000 --> 00:00:56,900
[Customer Success Manager] Also, would you want to customize the dashboard further to highlight key revenue trends?

14
00:00:57,500 --> 00:01:02,500
[Client] Yeah, actually, that would be helpful. If we could pull in a clearer view of our churn rate, that’d be great.

15
00:01:02,600 --> 00:01:08,200
[Customer Success Manager] Sure thing. We can create a custom widget for churn analysis, combining data from HubSpot and Stripe.

16
00:01:08,500 --> 00:01:11,000
[Client] Perfect. When could we have that ready to go?

17
00:01:11,500 --> 00:01:16,500
[Customer Success Manager] I’ll start working on it today. I should be able to have that updated by the end of the week. I’ll send you a preview before finalizing.

18
00:01:17,000 --> 00:01:19,800
[Client] That sounds good. Thanks for the quick turnaround.

19
00:01:20,000 --> 00:01:23,500
[Customer Success Manager] No problem! I'll also make sure to fix that Stripe integration issue.

20
00:01:24,000 --> 00:01:26,500
[Client] Awesome, I appreciate your help. Looking forward to seeing the changes!

21
00:01:27,000 --> 00:01:30,000
[Customer Success Manager] Great, have a good one, John. Talk to you soon!

22
00:01:30,500 --> 00:01:33,500
[Client] You too, take care!

"""