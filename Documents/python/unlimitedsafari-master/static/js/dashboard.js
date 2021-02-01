$(document).ready(function() {
        var acc_table = $("#safari-account-table");
        acc_table.DataTable({
            "processing": true,
            "serverSide": false,
            "ajax": {
                "url": '/dashboard/get-safari-accounts',
                dataSrc: "",
            },
            "columns": [
                {
                    "title": "Name",
                    "data": "name"
                },
                {
                    "title": "Email",
                    "data": "email"
                },
                {
                    "title": "Password",
                    "data": "password"
                },
                {
                    "title": "Expires At",
                    "data": "expires_at",
                }
            ],
        });
});