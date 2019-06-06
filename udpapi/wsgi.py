from udpapi.app import create_app

app = create_app()

# if __name__ == '__main__':
#     app = create_app()
#     import os
#     if os.environ.get('PORT') is not None:
#         app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
#     else:
#         app.run(debug=True, host='0.0.0.0')