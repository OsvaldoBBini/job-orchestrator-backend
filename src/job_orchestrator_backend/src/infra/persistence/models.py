from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

class Job(Base):
  __tablename__ = "jobs"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  name: Mapped[str] = mapped_column(String)
  owner: Mapped[str] = mapped_column(String)
  file_id: Mapped[str] = mapped_column(String)
  time_trigger: Mapped[str] = mapped_column(String)
  logs: Mapped[List["Log"]] = relationship(back_populates="job", cascade="all, delete-orphan")
  users: Mapped[List["UserJobPermission"]] = relationship(back_populates="job", cascade="all, delete-orphan")

class Log(Base):
  __tablename__ = "logs"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  log_id: Mapped[str] = mapped_column(String, ForeignKey("jobs.id", ondelete="CASCADE"))
  status: Mapped[str] = mapped_column(String)
  description: Mapped[str] = mapped_column(String)
  job: Mapped["Job"] = relationship("Job", back_populates="logs")
  
class User(Base):
  __tablename__ = "users"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  name: Mapped[str] = mapped_column(String)
  email: Mapped[str] = mapped_column(String)
  jobs: Mapped[List["UserJobPermission"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class PermissionLevel(Base):
  __tablename__ = "permission_levels"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  name: Mapped[str] = mapped_column(String)
  permissions: Mapped[List["UserJobPermission"]] = relationship(back_populates="permission")

class UserJobPermission(Base):
  __tablename__ = "user_job_permissions"
  id: Mapped[str] = mapped_column(String, primary_key=True)
  user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id", ondelete="CASCADE"))
  job_id: Mapped[str] = mapped_column(String, ForeignKey("jobs.id", ondelete="CASCADE"))
  permission_level_id: Mapped[str] = mapped_column(String, ForeignKey("permission_levels.id", ondelete="CASCADE"))
  user: Mapped["User"] = relationship("User", back_populates="jobs")
  job: Mapped["Job"] = relationship("Job", back_populates="users")
  permission: Mapped["PermissionLevel"] = relationship("PermissionLevel", back_populates="permissions") 

