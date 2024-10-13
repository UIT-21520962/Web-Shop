<script type="text/javascript">
  $(document).ready(function() {
    $('.add-btn').click(function(event) {
      event.preventDefault();
      var courseId = $(this).data('course');
      var url = "{% url 'register_course' %}";
      $.ajax({
        url: url,
        type: 'POST',
        data: {
          'course_id': courseId,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
          if (response.status === 'success') {
            alert('Đăng ký khóa học thành công!');
          } else {
            alert('Có lỗi xảy ra, vui lòng thử lại.');
          }
        },
        error: function(response) {
          alert('Có lỗi xảy ra, vui lòng thử lại.');
        }
      });
    })}
  );
</script>
