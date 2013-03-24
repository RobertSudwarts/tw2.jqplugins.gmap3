<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)}> </div>

<script >
$(document).ready(function() {

  $('#${w.id}').gmap3(${w.options | n}, 
    function(e) {
      console.log(e);
    });
  });

</script>
