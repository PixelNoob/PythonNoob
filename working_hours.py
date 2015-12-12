totalpay = raw_input ("How much did you get paid this month?")
total_hours = 176
pay_per_hour = float(totalpay) / total_hours
print "ARS per hour", pay_per_hour
print "USD per Hour", pay_per_hour / 15
if pay_per_hour < 124:
    print "pobre"
if pay_per_hour > 125:
    print "Rico"
