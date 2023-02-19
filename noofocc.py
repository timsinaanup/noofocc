text = input("Enter any text")
final_text = ''
counted = 0
output_text = ''
for word in text :
    if word not in final_text:
        final_text = final_text + word
for each in final_text:
    counted = text.count(each)
    output_text = output_text + each + str(counted) + "  "
print(output_text)