my $target = 200;
my @coins = (1,2,5,10,20,50,100,200);
my @ways = (1);
 
for $coin (@coins) {
  $ways[$_] += $ways[$_-$coin] for $coin..$target;
}
 
print "Answer to PE31 = $ways[$target]";
