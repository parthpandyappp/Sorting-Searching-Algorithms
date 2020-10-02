<?php
 
function merge_sort($arr){
   if(count($arr) == 1 ) return $arr;
   $mid = count($arr) / 2;
   $left = array_slice($arr, 0, $mid);
   $right = array_slice($arr, $mid);
   $left = merge_sort($left);
   $right = merge_sort($right);
   return merge($left, $right);
}
 
function merge($left, $right){
   $res = array();
   while (count($left) > 0 && count($right) > 0){
      if($left[0] > $right[0]){
         $res[] = $right[0];
         $right = array_slice($right , 1);
      }else{
         $res[] = $left[0];
         $left = array_slice($left, 1);
      }
   }
   while (count($left) > 0){
      $res[] = $left[0];
      $left = array_slice($left, 1);
   }
   while (count($right) > 0){
      $res[] = $right[0];
      $right = array_slice($right, 1);
   }
   return $res;
}
 
$array = array(20,43,65,88,11,33,56,74);
$sorted = merge_sort($array);
print_r($sorted);
 
?>