import datetime

from bp_btc_com.explorer import Explorer
from time import sleep

sleep_time = .5  # don't overstep rate limits
# get latest block
print(Explorer("btc").get_block())
sleep(sleep_time)

print(Explorer("bch").get_block())
sleep(sleep_time)

print(Explorer("bsv").get_block())
