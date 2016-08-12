$(document).ready(function() {
	// ############ Google OAuth ###########################
	function google_service_provider(data){
      var postData = {
		  "token": data['hg']['id_token'],
		  "provider":  "accounts.google.com",
		};
       $.ajax({
       	url:'http://127.0.0.1:8000/api/public_provider_login/',
       	data:JSON.stringify(postData),
       	processData:false,
       	contentType:'application/json',
       	dataType:'json',
       	type:'POST',
       	success:function(token_info){

	       	}
       });		
		
	}

	// ############ USERNAME PASSWORD SIGNUP ##################
    $('.btn-signup-username-password').click(function(e) {
      e.preventDefault();
      var postData = {
		  "username": $('#username').val(),
		  "password": $('#password').val(),
		};
       $.ajax({
       	url:'/api/signup/',
       	data:JSON.stringify(postData),
       	processData:false,
       	contentType:'application/json',
       	dataType:'json',
       	type:'POST',
       	//crossDomain:true,
       	success:function(res){
	       		console.log(res);
	       	}
       });
    });

	// ############ USERNAME PASSWORD LOGIN ##################
    $('.btn-login-username-password').click(function(e) {
      e.preventDefault();
      var postData = {
		  "username": $('#username').val(),
		  "password": $('#password').val(),
		};
       $.ajax({
       	url:'/api/admin_initiate_user/',
       	data:JSON.stringify(postData),
       	processData:false,
       	contentType:'application/json',
       	dataType:'json',
       	type:'POST',
       	//crossDomain:true,
       	success:function(res){
	       		console.log(res);
	       	}
       });
    });

    // GET OTP
    $('.btn-login-get-sms-otp').click(function(e){
		e.preventDefault();
		var phone_number = $('#phone_number').val();
		
		var postData = {
			"client_id":"klt93qPegFLny4h9FUsjhjcfUPrNCJnn",
			"connection":"smsdev",
			"phone_number": phone_number
		};
    	$.ajax({
	       	url:"https://" + AUTH0_DOMAIN + "/passwordless/start",
	       	data:JSON.stringify(postData),
	       	processData:false,
	       	contentType:'application/json',
	       	dataType:'json',
	       	type:'POST',
	       	success:function(res){
	       		console.log(res);
	       	}
       });
    });
    
    
    // ########## SMS OTP LOGIN #####################
    $('.btn-login-sms-otp').click(function(e) {
      e.preventDefault();
      /*var postData = {
          	response_type:'code',     // code - server side flows | token - client side flows
			client_id:AUTH0_CLIENT_ID, // {client-name}
			connection:'google-oauth2',
			redirect_uri:'http://127.0.0.1:8000/api/gettokenfromcode/'
       };*/
      var postData = {
		  "client_id":   "klt93qPegFLny4h9FUsjhjcfUPrNCJnn",
		  "connection":  "smsdev",
		  "grant_type":  "password",
		  "username":    "+919535862720",
		  "password":    $('#otp').val(),
		  "scope":       "openid name email"
		};
       $.ajax({
	       	url:'https://' + AUTH0_DOMAIN + "/oauth/ro/",
	       	data:JSON.stringify(postData),
	       	processData:false,
	       	contentType:'application/json',
	       	dataType:'json',
	       	type:'POST',
	       	success:function(token_info){
	       		var postData = token_info;
	    		$.ajax({
			       	url:'http://127.0.0.1:8000/api/gettokenfromfrontend/',
			       	data:JSON.stringify(postData),
			       	processData:false,
			       	contentType:'application/json',
			       	dataType:'json',
			       	type:'POST',
			       	success:function(res){
			       		console.log(res);
			       		localStorage.setItem('token', res['token_info']['id_token']);
			    		localStorage.setItem('profile', JSON.stringify(res['user_info']));
			       	}
	       		});
	       	}
       });
    });
});
