<h1 align="center">Setup of a stage for the game MoveHero offline version</h1>
<p align="justify">This is the creation of a sequence of falls for MoveHero game - offline version - It's look like the online version and you can see how it works in <a href="www.movehero.com.br">www.movehero.com.br</a></p>

<p align="justify">Developed at the School of Arts Sciences and Humanities of the University of São Paulo (EACH-USP). The game presents balls that fall, in four imaginary columns on the computer screen, within limits of interval between the falls and distribution between the columns predetermined by the researcher. The task is not to let balls fall. However, the balls can only be touched when they reach four circles placed parallel (in two height levels), two to the left and two to the right of the participant
(0 0 \o/ 0 0). Named targets 1, 2, 3 and 4, as viewed from left to right. The game captures the participant's movements through a webcam, not requiring physical contact to perform the task.</p>

<p align="justify">Later, when the configuration is approved by the researcher, the last line will be used to create a json file, in the format that the offline game reads.</p>

<h3>It must do</h3>
<p>Define the time of the game;</p>
<p>Create a sequence of falls randomly, within an estimated percentage distribution between columns. The researcher may choose a % of falls for each collumn and the randomly distribution must respect as good as possible;</p>
<p>Select a randon time inside a range of minimum and maximum posibles for each fall;</p>
<p>Choose whether or not the balls can be repeated sequentially in the same position and, if it have choosem to not repeat, no more tham 2 balls may fall in sequence in the same position;</p>
<p>The researcher may delay or anticipate the time interval of a ball that is repeated;</p>
<p>The researcher may delay or anticipate the time interval of a ball thaf fall in the oposite corner than your previous one. eg.: collumns 1 and 4, or collumns 4 and 1 in sequence;</p>
 <p>The report must include the sequence of falls, the totals and % per collumn, external and internal collumns, left and right colluns;</p>
 <p>The report must include a line to be copied to a json file if necessary in the same model that the game uses. eg.: ["",[times_of_collumn_1], [times_of_collumn_2], [],[times_of_collumn_3], [times_of_collumn_4]]</p>

