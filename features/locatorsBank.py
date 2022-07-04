class locatorsBank:
    #XYZ bank login page
    bank_manager_btn = "//button[contains(text(),'Bank Manager Login')]"

    #add a new customer
    add_cust_btn = "//button[normalize-space()='Add Customer'"
    cust_input_name = "/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/input[1]"
    cust_input_lname = "/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/input[1]"
    cust_input_postal = "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
    submit_cust = "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]"

    #search customer
    cust_btn = "//body/div[1]/div[1]/div[2]/div[1]/div[1]/button[3]"
    search_field = "//input[@placeholder='Search Customer']"


    #test customer
    name = "//td[contains(text(),'Ani')]"
    lname = "//td[contains(text(),'san')]"
    postal_code = "//td[contains(text(),'7777')]"

    #delete customer
    delete_btn = "//tbody/tr[6]/td[5]/button[1]"

