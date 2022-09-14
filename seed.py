from models import User, Listing
from app import db

db.drop_all()
db.create_all()

u1 = User(
    username="bryan",
    password="password",
    email="bryan@email.com",
    bio="Hello, world."
)

u2 = User(
    username="francis",
    password="password",
    email="francis@email.com",
    bio="Hello, world."
)

l1 = Listing(
    title="Luxe Oasis",
    description="Relaxing pool for the summertime",
    location="Dubrovnik, Croatia",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House1.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMSJGMEQCIGETgiNzmp1fHbTCR40guAvt6GuA32%2FJMDQtvC9S3jbfAiAOpghVr53tsS%2BZN8PxgfZvuNa2oFMvtkUN9dLBiW3VFSrtAgir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU1ODIxNDI1NDg4MyIM4k46mJ7vcHpmAo35KsEChZoS91b1qy8M2ZzVAuEGuZ7yfzqwVF2gaBbHPHAUYNQbRiAjYBJmsmMyM0bUUhPe2ZWKLIYjWySCtjNkUFb4JymN9k7Lwb08aNK%2B4%2BWj59S1uoyePNM4%2F0N26PED04g%2FNDo0AwLilwHJIivy7AswWWRuG3tWygq11yrdfIqwhDcbzpWhbrP3R9eZDX3uCinrcnRoPvly82v6SiZ9uOUVeX9aShIOb5%2BN%2Bl%2F%2FEGfuXslWRv%2Bi1rTrqFmrePBjFXkfNNFfrkY7aA2SZ%2F9zdwTpsVqkZjjFIQO0mxBiSr4K2LMmy08uTiD9kyxNtFBqloIzLzF7%2FKgXA7FIoYYp%2BVPmJClHhNUwCAOMxJ31lW%2BOlktu2zwZOiSo3NI%2BxdBmy3iaonA56EDVFtEsj%2FmvwnH%2FNf%2BHtQOlOYSxBMYurrj7bsOaMK%2BPg5kGOrQC0ooeUnEMeXPodLjXksJmLWincUhr8%2F%2Bk%2BmhrlfhZYFJpEJma8lCH2i1LCqEswIDTJgcAL7L5hknfjoO8jnqH9W6Z3maC55BBLbGMu7F8ckD1PHZmp%2FjdWAsWHfjnHhCRXEfk%2BYT1vZAoSQUnAhuBggJhtVk4O3VRv1afnAKh%2Ba2WItTNovbmhjcoeohFl%2FxvyS7mptxz%2FsdiU8l6c%2F3qvwg9gWvxV2VdvyR2SqxHjJvD%2BS1Vh4QeWv6AENS4DytoDmrqxXu%2Fhb02KmnEn%2FM%2FXk1%2B8CMdAGstS8Ur4slqO3sU68o2AwugAc6u297G%2Bicn5dj4qiJZpOw%2BmV%2FVXOZkvbmG%2FajpsY0GAzsboQXwqbT7iQ1uNFG6gJ%2BvmyKc%2B8w2Kqsb%2FV%2F5iq4nYW8hd1hMIKLLfJs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T055241Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSERQ2BBWHEE%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=103237c2d7030e76bbc170b95d21e3699dec9a416751e7dad0e5426b0d9ba677",
    price=400,
    created_by=u1.username
)

l2 = Listing(
    title="Beach View House",
    description="Stay as close to the ocean as you can get with waves right outside your door.",
    location="San Diego, California",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House2.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T063355Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=42172cb35bcb8cd4f285b44f9ec6f7f01be9f5eceec676c2fe77359cad410e7f",
    price=350,
    created_by=u2.username
)

l3 = Listing(
    title="Nipa Hut",
    description="Camp under the stars or bright moon, have a bonfire and feel its warmth against the cool breeze.",
    location="Boracay, Philippines",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House3.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T063509Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=d5635f24883d4373c30810ee74c6879612c741a3e0a95d637cb7b41a7abeb81f",
    price=200,
    created_by=u2.username
)

l4 = Listing(
    title="Modern Palm Springs Oasis",
    description="Backyard pool.",
    location="Palm Springs, California ",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House4.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T063611Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=754609ac5646b8f47727e155b8124326737f47cdb3ead20d66b224e34150f3a7",
    price=300,
    created_by=u1.username
)

l5 = Listing(
    title="Serene Lake Cabin",
    description="Dive into Lake Life",
    location="Copenhagen, Denmark",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House5.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T063830Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=d6af4f981dfadb6041dda4e1b105af54d87b8efdc673a1de8ca30cb489c2ddd3",
    price=350,
    created_by=u2.username
)

l6 = Listing(
    title="Tropical Beach House",
    description="Best view of of the best beach in Cuba.",
    location="Havana, Cuba",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House6.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T063908Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=9b75e6cf0ed72b9ed926786bbb139b67c2c48ab721bc106924fb5938756c6148",
    price=350,
    created_by=u2.username
)

l7 = Listing(
    title="Cabin in the Woods",
    description=" Great space for travelers that like to be cozy!",
    location="Vancouver, Canada",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House7.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T064026Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=997f597385f0abc1d48f4abf03126c61ea2698e55d7c2dcb1aac2bb6aac4f82d",
    price=350,
    created_by=u2.username
)

l8 = Listing(
    title="Luxe Cabin with a View",
    description="Explore the countryside at this popular 40-acre sanctuary",
    location="Edinburgh, Scotland",
    photo_url="https://fc-hosted-content.s3.us-west-2.amazonaws.com/share-bnb/House8.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMSJHMEUCIQCkja21%2FRdZkGOW8wZqEalZg246rDHGW8K%2FJv%2F0h3mnxAIgLe4fwJK0tak6u9DVG%2FefpTRKHqfjtcIQEnzVG60SIWwq7QIIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTgyMTQyNTQ4ODMiDFtZNK3%2FhKhZtQSqHyrBApVQHdPZqmdo5OIKcwgZIvX9FCEpiIA8EhDUCiH187%2FUI3CMojUjEtwfAmG%2BaFyeoas4sfLbtpnPDSpqcG4AheVnLZR5Yk%2B5L%2FNaDqVznFruNwEAQNXKGBdlfi1nvhHnC%2B1HWM8M0Rk1pwWXyWRZaqmhsCiiVlQ3ad4%2B3%2B3Ly34oUFJ5xoAH6%2BullzZhP4oCSyfMTIujsmuFZuyQMusgqh70wlTogamqh%2BthC%2BcIRaif%2FVzx5W9b54BXVt9g35q9Q5Y78zUt8DsYzN5xrgfJpeUV5gUT5zlIAdtKVLOBy71Yl3yeGdiWmDzuhV%2F7%2Fj9uynBL5kglA9KFn5Tt8EdXG81Srfy5CKrIl4k7pPMH5LCXW2YG7b99wLYocBHKQqE4PBdC%2F9fu0rDAAmysvsNdJQ5vP4y0gHgJucMUyGnxso0xyDCe4YWZBjqzAiHUl2k8aedGajbE7CcEcRn5c1dH%2ForzPWZxpiiKIxHCaIRf7YF7Lgbh7nUahKyMCXuRkQOZ1dU2sSysdcX1163ETlXoxrD5ru30EDRLGOQUqdSk6QaqpW4EbPOyRFazyGsCCysQZFirbdBh3NYL9c%2FTQ53%2BNm9fok8wqkiaLAX0oSyldz4PtcFovXZu21eHXbFYuBDkYmN%2Fj1aRJ9M98xZEC75m7D9vOTxDr6UvRzaUTPU7kV%2BH1LTQyFsQzysEDTSuCW6Ae08fQhdL7czL7muwbs0gbZBJeD2RMEWtEZYqW4IG595VR5x5MU8Cp9RyF41eYW4JdvtAI5gJETbNqaJknCwdeT76nZpnI4S7kwvo6bZ4SV7bVAxSk0UlFkc3jU%2FoExv71qYautC69bNTgZ9fOJA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220914T064050Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYD6BJSER7ISJUGME%2F20220914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=f0f28ace4f733ef4b7ac60f30a6d97e893aea9c4f7ea37c2fd20327cb35d7af2",
    price=350,
    created_by=u2.username
)


db.session.add_all([u1, u2, l1, l2, l3, l4, l5, l6, l7, l8])
db.session.commit()
