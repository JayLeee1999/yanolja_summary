from sqlalchemy import Column, ForeignKey, Integer, Text, Float
from database import Base

# 숙소정보
class AccommodationInfo(Base):
    __tablename__ = 'accommodation_info'
    id = Column(Integer, primary_key = True)
    name = Column (Text)
    address = Column(Text)
    phone_number = Column(Text)
    rating = Column(Float)

    # __repr__ 메서드는 객체를 문자열로 표현하기 위해 사용
    # 여기서는 <AccommodationInfo id> 형식의 문자열을 반환하도록 정의되
    # repr() 함수를 호출하면 <AccommodationInfo 1>과 같은 문자열이 반환
    # 주로 개발 및 디버깅 목적으로 사용
    def __repr__(self):
        return '<AccommodationInfo %r>' % (self.id)

# 숙소 리뷰 : 리뷰 ID, 숙소 ID, 리뷰 내용, 리뷰 평점, 리뷰 작성일
class AccommodationReview(Base):
    __tablename__ = 'accommodation_review'
    id = Column(Integer, primary_key=True)
    accommodation_id = Column(Integer, ForeignKey('accommodation_info.id'), nullable=False)   # 숙소 ID (외래 키)
    review = Column(Text)
    stars = Column(Integer)
    date = Column(Text)

    def __repr__(self):
        return '<AccommodationReview %r>' % (self.id)
    
# 리뷰 요약 : 리뷰 ID, 숙소 ID, 리뷰 요약 내용
class ReviewSummary(Base):
    __tablename__ = 'review_summary'
    id = Column(Integer, primary_key=True)
    accommodation_id = Column(Integer, ForeignKey('accommodation_info.id'), nullable=False)   # 숙소 ID (외래 키)
    summary_good = Column(Text)
    summary_bad = Column(Text)
    date = Column(Text)

    def __repr__(self):
        return '<ReviewSummary %r>' % (self.id)