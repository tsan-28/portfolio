#Imports the string module for character sets and the random module for random string generation.
import string, random 
#Imports the slugify function to create URL-safe slugs from text 
from django.utils.text import slugify 

#This function generates a random string of a specified size (defaulting to 10).
#chars: Specifies the set of characters to choose from. The default is lowercase letters and digits. This helps make the generated slugs more unique.
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
	#Uses a list comprehension and random.choice to select random characters from the chars string and joins them together to form the random string.
	return ''.join(random.choice(chars) for _ in range(size)) 

def unique_slug_generator(instance, new_slug = None):
	if new_slug is not None: 
		# If no initial slug is provided, it generates a slug from the instance.user.username (assuming the instance is a Profile object
		slug = new_slug

	else: 
		# Gets the class of the instance (e.g., Profile).
		slug = slugify(instance.user.username) 
	Klass = instance.__class__ 
	#Determines the maximum length allowed for the slug field from the model's definition. This is essential to avoid slug values that are too long for the database column, which would cause an error.
	max_length = Klass._meta.get_field('slug').max_length 
	#Truncates the initial slug to the maximum allowed length. This prevents potential issues when slugifying long usernames.
	slug = slug[:max_length] 
	#Checks if a model instance with the generated slug already exists in the database.
	qs_exists = Klass.objects.filter(slug = slug).exists() 
	
	#If the slug already exists, a new slug is created by appending a hyphen and a random string.
	if qs_exists: 
		#Before appending the random string, the original slug is truncated by the length of the random string plus the dash. This is to ensure that the resulting slug does not exceed the max_length of the slug field.
		new_slug = "{slug}-{randstr}".format( 
			#generates a random string of length 4.
			slug = slug[:max_length-5], randstr = random_string_generator(size = 10)) 
			# Recursively calls the function with the new, potentially unique slug to check for conflicts.
		return unique_slug_generator(instance, new_slug = new_slug) 
	# If no conflict is found, the generated slug is returned
	return slug


