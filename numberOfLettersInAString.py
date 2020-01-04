def numberOfLettersInAString(string):
  count=1
  length=""
  if len(string)>1:
    for i in range(1,len(string)):
      if string[i-1]==string[i]:
        count+=1
      else :
        length += str(count)+string[i-1]
        # length += string[i-1]+" repeats "+str(count)+", "
        count=1
    # length += ("and "+string[i]+" repeats "+str(count))
    length += str(count)+string[i]
  else:
    i=0
    # length += ("and "+string[i]+" repeats "+str(count))
    length += str(count)+string[i]
  return(length)
