<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)}> </div>

<script type="text/javascript">

$(document).ready(function() {
  $('#${w.id}').width('${w.width}').height('${w.height}').gmap3(
  	${w.options | n}
   );
});  

</script>
