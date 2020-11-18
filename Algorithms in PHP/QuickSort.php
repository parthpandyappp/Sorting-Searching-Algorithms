<?php
 
    $unsorted_numbers = array(20,43,65,88,11,33,56,74);
 
    function quicksort($array)
    {
        if (count($array) == 0)
            return array();
 
        $pivot_element = $array[0];
        $left_element = $right_element = array();
 
        for ($i = 1; $i < count($array); $i++) {
            if ($array[$i] <$pivot_element)
                $left_element[] = $array[$i];
            else
                $right_element[] = $array[$i];
        }
 
        return array_merge(quicksort($left_element), array($pivot_element), quicksort($right_element));
    }
 
    $sorted_numbers = quicksort($unsorted_numbers);
 
    print_r($sorted_numbers);

    ?>