from flask import Flask,jsonify,request
from database import users,session
app=Flask(__name__)


#Signup API
@app.route('/Signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        Email=request.form["email"]
        Username=request.form["username"]
        Password=request.form["password"]
        ConfirmPassword=request.form["confirmpassword"]
            
        email= session.query(users).filter_by(email=Email).first()
        username=session.query(users).filter_by(username=Username).first()
        
        if not email and not username:
            if Password==ConfirmPassword:
                register= users(username=Username,email=Email,password=Password)
                
                session.add(register)
                session.commit()
                
                return jsonify(
                    message = 'Account Created Successfully!',
                    status=200
                )
                
            return jsonify(
                message = "Password does not match!",
                status=200
            )
        
        else:
            return jsonify(
                    message = 'User Already Exists!',
                    status=200
                )
        
    else:
        return jsonify(
                message = 'Unauthorized',
                status=401,
            )
        


#Login API
@app.route('/Login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        Username = request.form["username"]
        Password = request.form["password"]
        
        login = session.query(users).filter_by(username=Username,password=Password).first()
        
        if not login:
            return jsonify(
                    message = 'Login Failed!',
                    status=200
                )
            
        else:
            return jsonify(
                message = 'Login Successful!',
                status=200,
                Username=Username
            )
            
    else:
        return jsonify(
                message = 'Unauthorized',
                status=401,
            )
        
            
            


    
    

if __name__=='__main__':
    app.run(debug=True)