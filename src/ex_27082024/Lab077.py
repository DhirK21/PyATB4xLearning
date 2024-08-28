public_toilet = "PB"

# local variables have more preference as compare to public variables

def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)


home()
print("******************")

def strange():
    print(public_toilet)
    # print(private_toilet)

strange()
print("******************")

print(public_toilet)
# print(private_toilet)