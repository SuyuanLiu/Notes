def main():
  global count
  count = 0
  print(count)

def test():
  global count 
  count += 1

if __name__ == '__main__':
  main()
  test()
  print(count)
