(function(){
    if (typeof motu !== 'undefined' && motu !== "") {
        var iframe;

        // IE workaround (fix for quirks mode default)
        try {
            iframe = document.createElement('<iframe name="motimatic_iframe"></iframe>');
        } catch(e) {
            iframe = document.createElement('iframe');
            iframe.name = 'motimatic_iframe';
        }

        // Create the iframe and add it to the body
        iframe.id = 'motimatic_iframe';
        iframe.src = 'about:blank';
        iframe.style.display = 'none';

        document.body.appendChild(iframe);

        
            var customerIDInput;
            var constituentIDInput;

            // IE workaround (fix for quirks mode default)
            try {
                customerIDInput = document.createElement('<input name="customer_id" />');
                constituentIDInput = document.createElement('<input name="constituent_id" />');
                serveCustomerInput = document.createElement('<input name="serve_customer" />');
            } catch(e) {
                customerIDInput = document.createElement('input');
                customerIDInput.name = 'customer_id';

                constituentIDInput = document.createElement('input');
                constituentIDInput.name = 'constituent_id';

                serveCustomerInput = document.createElement('input');
                serveCustomerInput.name = 'serve_customer';
            }

            // Create the form and add it to the body
            var dataForm = document.createElement('form');
            dataForm.id = 'motimatic_data_form';
            dataForm.target = 'motimatic_iframe';
            dataForm.action = 'https://t.motimatic.com/engine/v2/pixels/secure/';
            dataForm.method = 'POST';
            dataForm.style.display = 'none';

            customerIDInput.type = 'text';
            customerIDInput.value = '';
            dataForm.appendChild(customerIDInput);

            constituentIDInput.type = 'text';
            constituentIDInput.value = '';
            dataForm.appendChild(constituentIDInput);

            constituentIDInput.type = 'text';
            constituentIDInput.value = '';
            dataForm.appendChild(constituentIDInput);

            serveCustomerInput.type = 'text';
            serveCustomerInput.value = '';
            dataForm.appendChild(serveCustomerInput);

            var submitInput = document.createElement('input');
            submitInput.type = "submit";
            dataForm.appendChild(submitInput);

            document.body.appendChild(dataForm);

            // Submit the form with the provided customer and constituent IDs
            var motc_to_send = motc;
            if (motc.substring(0, 3) == 'CU_'){
                motc_to_send = motc.substring(3);
                dataForm.elements.serve_customer.value = 'yes';
            }
            else {
                dataForm.elements.serve_customer.value = 'no';
            }

            dataForm.elements.customer_id.value = motc_to_send;
            dataForm.elements.constituent_id.value = motu;

            dataForm.submit();
        
    } else {
        console.log("Motimatic JS: 'motu' is blank or not set.");
    }
})();
