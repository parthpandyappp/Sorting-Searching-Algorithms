mmerge<-function(a,b) {
    r<-numeric(length(a)+length(b))
    ai<-1; bi<-1; j<-1;
    for(j in 1:length(r)) {
        if((ai<=length(a) && a[ai]<b[bi]) || bi>length(b)) {
            r[j] <- a[ai]
            ai <- ai+1
        } else {
            r[j] <- b[bi]
            bi <- bi+1          
        }
    }
    r
}
mmergesort<-function(A) {
    if(length(A)>1) {
        q <- ceiling(length(A)/2)
        a <- mmergesort(A[1:q])
        b <- mmergesort(A[(q+1):length(A)])
        mmerge(a,b)
    } else {
        A
    }
}

x<-c(18, 16, 8, 7, 6, 3, 11, 9, 15, 1)
mmergesort(x)
