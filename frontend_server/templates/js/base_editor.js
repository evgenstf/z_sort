<script>
var content = document.getElementById("content");
var ghost_footer = document.getElementById("ghost_footer");

rect = content.getBoundingClientRect();
ghost_footer.style.height = 70 + "px";

</script>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({"fast-preview": {disabled: true}, tex2jax: {preview: "none", inlineMath: [['$','$'], ['\\(','\\)']]}});

  document.getElementById("content").setAttribute("style", "visibility:hidden");
  MathJax.Hub.Queue(
    function () {
      document.getElementById("content").setAttribute("style", "");
    }
  );
</script>
