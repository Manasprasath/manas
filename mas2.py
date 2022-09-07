def solve(s, t):
   if len(s) != len(t):
      return False
 
   s = sorted(s)
   t = sorted(t)
 
   return s == t

s = "bit"
t = "biet"
print(solve(s, t))
