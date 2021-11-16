# imports here


# you will have 1 @app.route for each html document
# 1 @app.route for each form 

# so to start 5 render_templates 6 redirect (hidden or processing) routes (the forms + delete & logout)

# @app.route('/') # these would be for rendering html
# @app.route('/', methods=['post']) # these would be for processing forms

# make sure each def  for each route is a different name createItem register, things that also denote what they are for helps