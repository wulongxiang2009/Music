CMProcessBar4::CMProcessBar4(QWidget *parent) : QWidget(parent)
{
    timer = new QTimer;
    connect(timer,QTimer::timeout,this,[=](){
        rRange+=40;
        if(rRange>=360){
            rRange = 0;
        }
        update();
    });
}

void CMProcessBar4::paintEvent(QPaintEvent *event){
    int width = this->width();
    int height = this->height();
    int side = qMin(width, height);
    QPainter painter(this);
    painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);
    painter.translate(width / 2, height / 2);
    painter.scale(side / 200.0, side / 200.0);

    paintE(&painter);
}

void CMProcessBar4::paintE(QPainter* painter){
    int range = 360.0/eCount;
    painter->save();
    painter->rotate(rRange);
    painter->setPen(Qt::NoPen);
    painter->setBrush(Qt::white);
    painter->drawEllipse(QPoint(oERange,0),eRange,eRange);
    painter->setBrush(QColor("#E4E4E4"));
    for(int i = 0;i<eCount-1;i++){
        painter->rotate(range);
        painter->drawEllipse(QPoint(oERange,0),eRange,eRange);
    }
    painter->restore();
}

void CMProcessBar4::startR(){
    timer->start(100);
}

