<script>
var content = document.getElementById("content");
var ghost_footer = document.getElementById("ghost_footer");

rect = content.getBoundingClientRect();
ghost_footer.style.height = Math.max(10, window.innerHeight - rect.bottom - 44) + "px";

</script>
