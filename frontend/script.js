$(document).ready(function() {
    $("#messageArea").on("submit", function(event) {
        event.preventDefault();
        const date = new Date();
        const hour = date.getHours();
        const minute = date.getMinutes();
        const str_time = hour + ":" + (minute < 10 ? "0" + minute : minute);
        var rawText = $("#text").val();
        if(!rawText) return;

        // Append user message
        var userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + rawText + '<span class="msg_time_send">'+ str_time +'</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
        $("#text").val("");
        $("#messageFormeight").append(userHtml);
        $("#messageFormeight").scrollTop($("#messageFormeight")[0].scrollHeight);

        // Send to FastAPI
        $.ajax({
            url: "/ask",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({question: rawText}),
            success: function(data) {
                var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="https://cdn-icons-png.flaticon.com/512/387/387569.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + data.answer + '<span class="msg_time">' + str_time + '</span></div></div>';
                $("#messageFormeight").append(botHtml);
                $("#messageFormeight").scrollTop($("#messageFormeight")[0].scrollHeight);
            }
        });
    });
});
