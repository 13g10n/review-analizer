from model.analizer import Analizer

if __name__ == '__main__':
    text = '''What evidence can you share that demonstrates the impact of the engagement? 

I’ve had multiple people comment positively on the clean branding, the site, and elements they’ve helped pull together. 

How did DEKSIA perform from a project management standpoint? 

I've worked with multiple agencies over the years, and DEKSIA are among the best communicators. We communicate through email and regular conference calls. Lauren is great about keeping in touch. If I have a question about my project, they respond very quickly, which is unusual for an agency. 

What did you find most impressive about them? 

They’re great at putting themselves in the client’s shoes and are fun to work with. You can tell Lauren is passionate about what he does. The whole team is very good at what they do and have many ideas to provide me. They’re always on their toes and see the project from my standpoint instead of just trying to make money and move on. They truly care about what they’re doing, and it shows throughout the whole process. 

Are there any areas they could improve? 

No. 

Do you have any advice for potential customers? 

The best thing you can do is fully communicate what you’re trying to do, whether it be your vision or its strategic implementations. Give them as much detail as possible. Once you do that, they will take it and run with it.
второй
Could you share any evidence that would demonstrate the productivity, quality of work, or the impact of the engagement? 

Quantitatively we don't have any metrics, but qualitatively we've gotten great feedback from people who see our name and now see the connection between our name and our organization. 

How did Deksia perform from a project management standpoint? 

They are excellent at project management. Aaron is the main guy who serves as their project manager, and he is always available by phone, email, or text, and will respond to you within the hour. Corey was another team member who we worked with directly, and he was also incredibly helpful. 

What did you find most impressive about Deksia? 

What sets them apart is Aaron's deep knowledge of our business. What our company does is not something that an everyday person has common knowledge of, for instance running a restaurant or a similar business, but Aaron takes the time to really understand us and the intricacies of our company which we really appreciate and had led us to a successful outcome with our new name and branding campaign. 

Are there any areas Deksia could improve? 

I don't think there's anything they can improve upon at this point.'''
    Analizer.process_text(text)

