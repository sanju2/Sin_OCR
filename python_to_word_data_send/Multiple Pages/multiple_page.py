# Try example number two where we create multiple pages
# Define a dictionary for 3 customers
cust_1 = {
    'status': 'Gold',
    'city': 'Springfield',
    'phone_number': '800-555-5555',
    'Business': 'Cool Shoes',
    'zip': '55555',
    'purchases': '$500,000',
    'shipping_limit': '$500',
    'state': 'MO',
    'address': '1234 Main Street',
    'date': '{:%d-%b-%Y}'.format(date.today()),
    'discount': '5%',
    'recipient': 'Mr. Jones'
}

cust_2 = {
    'status': 'Silver',
    'city': 'Columbus',
    'phone_number': '800-555-5551',
    'Business': 'Fancy Pants',
    'zip': '55551',
    'purchases': '$250,000',
    'shipping_limit': '$2000',
    'state': 'OH',
    'address': '1234 Elm St',
    'date': '{:%d-%b-%Y}'.format(date.today()),
    'discount': '2%',
    'recipient': 'Mrs. Smith'
}

cust_3 = {
    'status': 'Bronze',
    'city': 'Franklin',
    'phone_number': '800-555-5511',
    'Business': 'Tango Tops',
    'zip': '55511',
    'purchases': '$100,000',
    'shipping_limit': '$2500',
    'state': 'KY',
    'address': '1234 Adams St',
    'date': '{:%d-%b-%Y}'.format(date.today()),
    'discount': '2%',
    'recipient': 'Mr. Lincoln'
}

document_2 = MailMerge(template_1)
document_2.merge_pages([cust_1, cust_2, cust_3])
document_2.write('example2.docx')

# Final Example includes a table with the sales history

sales_history = [{
    'prod_desc': 'Red Shoes',
    'price': '$10.00',
    'quantity': '2500',
    'total_purchases': '$25,000.00'
}, {
    'prod_desc': 'Green Shirt',
    'price': '$20.00',
    'quantity': '10000',
    'total_purchases': '$200,000.00'
}, {
    'prod_desc': 'Purple belt',
    'price': '$5.00',
    'quantity': '5000',
    'total_purchases': '$25,000.00'
}]

document_3 = MailMerge(template_2)
document_3.merge(**cust_2)
document_3.merge_rows('prod_desc', sales_history)
document_3.write('example3.docx')
