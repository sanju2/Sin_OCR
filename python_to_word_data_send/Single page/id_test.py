from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

# Define the templates - assumes they are in the same directory as the code
template_1 = "id_details.docx"

# Show a simple example
document_1 = MailMerge(template_1)
print("Fields included in {}: {}".format(template_1,
                                         document_1.get_merge_fields()))

# Merge in the values
document_1.merge(
    name='sanju',
    age='18',
    place='amabalngoda')

# Save the document as example 1
document_1.write('example1.docx')

