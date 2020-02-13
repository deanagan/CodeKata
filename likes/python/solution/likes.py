
def likes(likers):
   likelookup = {
   	0: 'no one likes this',
   	1: '{} likes this',
   	2: '{} and {} like this',
   	3: '{}, {} and {} like this'
   	}
   default = f'{{}}, {{}} and {len(likers) - 2} others like this'
   fmtlikestr = likelookup.get(len(likers), default)
   return fmtlikestr.format(*likers)