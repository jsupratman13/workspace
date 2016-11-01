#Extra Notes

##When to use filters?
###particle filter
* pros: easy to implement
* cons: complexity scales exponentially with number of dimension -> cant apply to high dimension, if loose track of correct hypothesis, never regains it
###kalman filter
* pros: only filter that does scale exponentially
* cons: unimodal, cant have multiple hypotheses
###histogram filter
* pros: global uncertainty is solved systematically, grid based lot of programming framwork support it, can regain correct hypothesis
* cons: limitation is the resolution of the grid

###Conclusion
* If you have multimodal distribution use particle filter is you can
* Continous space with unimodal distribution use kalman filter
* Switch between filter is not used oftern. The switch can cause moment of uncertainty and that is deadly in robotics
* Mix filter -> Rao-Blackwwellized filter
* Computation vs Accuracy: if normalize weight is high, you can have less particle
* When tracking is good, fewer particles is okay
