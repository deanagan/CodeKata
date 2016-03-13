Write code that determines whether you need to delete,swap two letters or add a letter in order to
make two words the same. There are cases where two words are not gonna be ever the
same. In that case, return "IMPOSSIBLE". Limit the deletion or addition to only one letter and limit
to only one swap. The comparisons are case insensitive.

Examples:

Source = FROM   Target = FORM   Return = SWAP R WITH O
Source = FORM   Target = FROM   Return = SWAP O WITH R
Source = NIECE  Target = NICE   Return = DELETE E
Source = NICE   Target = NIECE  Return = ADD E
Source = HELLO  Target = HI     Return = IMPOSSIBLE
