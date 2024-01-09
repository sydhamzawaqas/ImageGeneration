from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

number_of_images = 1

for i in range(number_of_images):
    response = client.images.generate(
        model="dall-e-2",
        prompt="""In the dense, ancient woods of 10th-century Canada, a stoic Norse warrior clad in traditional armor, wielding a battle axe, finds himself in an unexpected scenario. Mounted on a majestic steed, the warrior navigates the terrain amidst the chaos of a massive spill of amber-colored maple syrup. His expression is one of steely determination mixed with disbelief as his horse struggles to maintain balance on the syrupy mess.""",
        size="1024x1024",
        quality="standard",
        n=1, 
    )
    
    image_url = response.data[0].url
    print(f"Image {i + 1} URL: {image_url}")
