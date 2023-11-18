from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE1 = """ Sam Altman has been fired as CEO of OpenAI, the company announced on Friday.

“Mr. Altman’s departure follows a deliberative review process by the board, which concluded that he was not consistently candid in his communications with the board, hindering its ability to exercise its responsibilities,” the company said in its blog post. “The board no longer has confidence in his ability to continue leading OpenAI.”

Chief technology officer Mira Murati will be the interim CEO, effective immediately. The company will be conducting a search for a permanent CEO successor. When contacted by The Verge, OpenAI’s communications department declined to comment beyond the blog post. Employees at OpenAI found out about the news when it was announced publicly, according to multiple sources.

“I loved my time at OpenAI,” Altman said in a post on X (formerly Twitter). “It was transformative for me personally, and hopefully the world a little bit.” In a follow-up post, he described the experience of his firing as “sorta like reading your own eulogy while you’re still alive.”
OpenAI’s announcement also said that co-founder and president Greg Brockman will be stepping down as chairman of the board but remain at the company. Hours after it was published, Brockman posted to X that he had quit “based on today’s news.”Later, in another post on X, Brockman said he and Altman were both notified of their removal from the board on Friday by OpenAI co-founder and chief scientist Ilya Sutskever, who is also a board member. “Sam and I are shocked and saddened by what the board did today,” Brockman wrote.This is an extremely sudden turn of events. Altman has been the face of OpenAI, which kick-started the current AI arms race with last year’s hugely popular release of ChatGPT. Just last week, Altman led the keynote at the company’s first-ever DevDay conference, where it announced a suite of major new updates to compete with other big tech companies like Microsoft and Google. More recently, Altman spoke at Thursday’s Asia-Pacific Economic Cooperation conference.Microsoft, which has invested billions in OpenAI, tells The Verge it will continue to partner with the company. “We have a long-term partnership with OpenAI and Microsoft remains committed to Mira and their team as we bring this next era of AI to our customers,” according to a statement sent by Microsoft spokesperson Frank Shaw. Microsoft CEO Satya Nadella made a similar statement on X.Altman has reportedly talked with Jony Ive, Apple’s former chief design officer, about making the “iPhone of artificial intelligence,” though Altman downplayed those rumors at a recent Wall Street Journal conference. He’s also the biggest shareholder in Humane, which just launched orders for its Humane AI Pin.

Altman is a co-founder of OpenAI and initially served as a co-chair of the company alongside Elon Musk. Musk left in 2018 to avoid a conflict of interest with Tesla. He has since founded his own AI company, xAI.

Unlike traditional private company boards, OpenAI’s board consists mostly of outsiders. After Altman and Brockman’s departures, its remaining board members are the company’s chief scientist, Ilya Sutskever, Quora CEO Adam D’Angelo, Tasha McCauley, the former CEO of GeoSim Systems, and Helen Toner, the director of strategy at Georgetown’s Center for Security and Emerging Technology.
"""

ARTICLE2 = """
OpenAI, the company behind the viral chatbot ChatGPT, fired its CEO and founder, Sam Altman, on Friday. His stunning departure sent shockwaves through the budding AI industry.

The company, in a statement, said an internal investigation found that Altman was not always truthful with the board.

“Mr. Altman’s departure follows a deliberative review process by the board, which concluded that he was not consistently candid in his communications with the board, hindering its ability to exercise its responsibilities,” the company said in its statement. “The board no longer has confidence in his ability to continue leading OpenAI.”
OpenAI announced Mira Murati, the company’s chief technology officer, will serve as interim CEO until a permanent successor is chosen.

In a tweet following the news, Altman said he “loved my time at openai.”

‘it was transformative for me personally, and hopefully the world a little bit. most of all i loved working with such talented people,” he said. “will have more to say about what’s next later.”

The news follows OpenAI’s first developer conference held in San Francisco last week, where Altman served as the master of ceremonies, unveiling a series of new artificial intelligence tool updates, including the ability for developers to create custom versions of ChatGPT. He also shared about 2 million developers now use the platform, and about 90% of Fortune 500 companies are using the tools internally. It currently has 100 million active users.ChatGPT launched late last year, making Altman an overnight quasi-celebrity and the face of a new crop of AI tools that can generate images and texts in response to simple user prompts. The technology is called generative AI and has since been deployed by Microsoft on its search engine and other tools. Google has a rival called “Bard,” and other generative AI tools have been developed in recent months.

Not long after its release, ChatGPT became a household name almost synonymous with AI itself. CEOs used it to draft emails, people built websites with no prior coding experience, and it passed exams from law and business schools.

Although Altman has long been an advocate of AI, he is also one of its biggest critics. In testimony before Congress earlier this year, Altman described the technology’s current boom as a pivotal moment.“Is [AI] gonna be like the printing press that diffused knowledge, power, and learning widely across the landscape that empowered ordinary, everyday individuals that led to greater flourishing, that led above all to greater liberty?” he said. “Or is it gonna be more like the atom bomb – huge technological breakthrough, but the consequences (severe, terrible) continue to haunt us to this day?”

He was also one of several tech CEOs to meet with White House leaders, including Vice President Kamala Harris and President Joe Biden, this year to emphasize the importance of ethical and responsible AI development.Others wanted Altman and OpenAI to move more cautiously. Elon Musk, who helped found OpenAI before breaking from the group, and dozens of tech leaders, professors and researchers in urged artificial intelligence labs like OpenAI to stop the training of the most powerful AI systems for at least six months, citing “profound risks to society and humanity.” (At the same time, some experts questioned if those who signed the letter sought to maintain their competitive edge over other companies.)

OpenAI declined CNN’s request for further comment.

Arun Chandrasekaran, an analyst at Gartner Research, called Altman’s exit “shocking,” as he’s been championing OpenAI’s cause with developers, consumers, regulators and others. “I am sure the OpenAI board took this decision after a lot of deliberation,” he said.

“OpenAI does have a deep bench of technical leaders and it will be interesting to see how its next generation of leaders steer by continuing its fast paced innovation culture, scaling the business and meeting the expectations of regulators and society at large.”

Murati was born and raised in Albania and studied engineering at Dartmouth. She joined OpenAI in 2018. Previously, she managed the product and engineering teams at augmented reality company Ultraleap (then called Leap Motion) and earlier worked at Tesla, where she helped develop the Model X.

The news shocked AI insiders, analysts and tech executives alike. Microsoft, which poured millions of dollars into Open AI earlier this year, told CNN in a statement it “remains committed to Mira and their team as we bring this next era of AI to our customers,” according to a company spokesperson.

Microsoft’s stock price slid 1.6% Friday and fell about another 1% in afterhours trading.

In a tweet, former Google CEO Eric Schmidt called Altman “a hero of mine.”

“He built a company from nothing to $90 Billion in value, and changed our collective world forever,” Schmidt said. “I can’t wait to see what he does next. I, and billions of people, will benefit from his future work- it’s going to be simply incredible. Thank you [Altman] for all you have done for all of us.”

Reece Hayden, an analyst at ABI Research, said this could be a “big blow” for commentators calling for AI regulation.

“Sam Altman has been a passionate advocate for this, and this could signal that OpenAI are leaning towards a more self-regulatory approach,” Hayden said.

"""
# print(summarizer(ARTICLE1, max_length=130, min_length=30, do_sample=False))

# print(summarizer(ARTICLE2, max_length=230, min_length=30, do_sample=False))
print(summarizer("gino the goat", max_length=130, min_length=30, do_sample=False))

# print(summarizer(ARTICLE2[len(ARTICLE2):], max_length=130, min_length=30, do_sample=False))